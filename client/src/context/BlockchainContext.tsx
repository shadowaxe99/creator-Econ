import React, { createContext, useContext, useState, useEffect, useCallback } from 'react';
import { IAsset } from '../interfaces/IAsset';
import { useWallet } from '../hooks/useWallet';
import { purchaseAssetOnBlockchain } from '../utils/blockchain';

interface BlockchainContextProps {
  assets: IAsset[];
  fetchAssets: () => void;
  purchaseAsset: (assetId: string) => Promise<void>;
}

const BlockchainContext = createContext<BlockchainContextProps | undefined>(undefined);

export const BlockchainProvider: React.FC = ({ children }) => {
  const [assets, setAssets] = useState<IAsset[]>([]);
  const { walletAddress } = useWallet();

  const fetchAssets = useCallback(async () => {
    try {
      const response = await fetch('/api/assets');
      const data = await response.json();
      setAssets(data);
    } catch (error) {
      console.error('Error fetching assets:', error);
    }
  }, []);

  const purchaseAsset = useCallback(async (assetId: string) => {
    if (!walletAddress) {
      console.error('Wallet address not found');
      return;
    }

    try {
      const transactionReceipt = await purchaseAssetOnBlockchain(assetId, walletAddress);
      if (transactionReceipt && transactionReceipt.status === 'success') {
        // Update local state to reflect the purchase
        setAssets(prevAssets =>
          prevAssets.map(asset =>
            asset.id === assetId ? { ...asset, isSold: true } : asset
          ),
        );
      } else {
        console.error('Transaction failed:', transactionReceipt);
      }
    } catch (error) {
      console.error('Error purchasing asset:', error);
    }
  }, [walletAddress]);

  useEffect(() => {
    fetchAssets();
  }, [fetchAssets]);

  return (
    <BlockchainContext.Provider value={{ assets, fetchAssets, purchaseAsset }}>
      {children}
    </BlockchainContext.Provider>
  );
};

export const useBlockchain = () => {
  const context = useContext(BlockchainContext);
  if (context === undefined) {
    throw new Error('useBlockchain must be used within a BlockchainProvider');
  }
  return context;
};
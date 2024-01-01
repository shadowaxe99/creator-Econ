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
      console.error('Failed to fetch assets. Please check the API endpoint and ensure the network is accessible:', error);
    }
  }, [setAssets]);

  const purchaseAsset = useCallback(async (assetId: string) => {
    if (!walletAddress) {
      throw new Error('Cannot purchase an asset without a valid wallet address');
    }

    try {
      const transactionReceipt = await purchaseAssetOnBlockchain(assetId, walletAddress);
      if (transactionReceipt && transactionReceipt.status === 'success') {
        // Update local state to reflect the purchase
        setAssets(prevAssets =>
          prevAssets.map(asset =>
            asset.id === assetId ? { ...asset, isSold: true } : asset
          )
        );
        // More functionalities could be implemented here as per requirement
      } else {
        throw new Error(
          `Transaction failed with status: ${transactionReceipt.status} and message: ${transactionReceipt.message}`
        );
      }
    } catch (error) {
      if (error instanceof Error) {
        console.error('Error purchasing asset:', error.message);
      } else {
        console.error('Unknown error occurred when purchasing asset');
      }
    }
  }, [walletAddress, setAssets]);

  useEffect(() => {
    fetchAssets();
  }, [fetchAssets]);

  // New blockchain functionalities
  const getTransactionHistory = useCallback(async (address: string) => {
    // Implement fetching transaction history
    // Ensure error handling is in place
  }, [/* Dependencies, if any */]);

  const getTransactionStatus = useCallback(async (transactionHash: string) => {
    // Implement fetching status of a transaction
    // Ensure error handling is in place
  }, [/* Dependencies, if any */]);

  return (
    <BlockchainContext.Provider value={{ assets, fetchAssets, purchaseAsset, getTransactionHistory, getTransactionStatus }}>
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
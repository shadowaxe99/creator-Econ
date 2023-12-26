import React, { useState, useEffect, useContext } from 'react';
import AssetItem from './AssetItem';
import { BlockchainContext } from '../context/BlockchainContext';
import { IAsset } from '../interfaces/IAsset';

const AssetList: React.FC = () => {
  const [assets, setAssets] = useState<IAsset[]>([]);
  const { blockchainService } = useContext(BlockchainContext);

  useEffect(() => {
    const fetchAssets = async () => {
      try {
        const response = await blockchainService.getAssets();
        setAssets(response);
      } catch (error) {
        console.error('Error fetching assets:', error);
      }
    };

    fetchAssets();
  }, [blockchainService]);

  const handlePurchase = async (assetId: string) => {
    try {
      const success = await blockchainService.purchaseAsset(assetId);
      if (success) {
        setAssets(assets.map(asset => asset.id === assetId ? { ...asset, isSold: true } : asset));
      } else {
        console.error('Purchase failed');
      }
    } catch (error) {
      console.error('Error purchasing asset:', error);
    }
  };

  return (
    <div className="asset-list">
      {assets.map(asset => (
        <AssetItem key={asset.id} asset={asset} onPurchase={handlePurchase} />
      ))}
    </div>
  );
};

export default AssetList;
import React, { useState, useEffect, useContext } from 'react';
import { BlockchainContext } from '../../context/BlockchainContext';
import AssetList from '../marketplace/AssetList';
import { IAsset } from '../marketplace/interfaces/IAsset';
import './CreatorDashboard.css'; // Assuming a corresponding CSS file for styling

const CreatorDashboard: React.FC = () => {
  const [assets, setAssets] = useState<IAsset[]>([]);
  const { blockchainService } = useContext(BlockchainContext);

  useEffect(() => {
    const fetchAssets = async () => {
      const ownedAssets = await blockchainService.getOwnedAssets();
      setAssets(ownedAssets);
    };

    fetchAssets();
  }, [blockchainService]);

  const handleAssetSale = async (assetId: string) => {
    const result = await blockchainService.sellAsset(assetId);
    if (result.success) {
      setAssets(assets.filter(asset => asset.id !== assetId));
    } else {
      alert('Sale failed: ' + result.message);
    }
  };

  return (
    <div className="creator-dashboard">
      <h1>My Assets</h1>
      <AssetList assets={assets} onAssetSale={handleAssetSale} />
    </div>
  );
};

export default CreatorDashboard;
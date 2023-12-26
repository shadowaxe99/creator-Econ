import React, { useContext } from 'react';
import { BlockchainContext } from '../../context/BlockchainContext';
import './AssetItem.css';

interface AssetItemProps {
  id: string;
  title: string;
  description: string;
  price: number;
  imageUrl: string;
}

const AssetItem: React.FC<AssetItemProps> = ({ id, title, description, price, imageUrl }) => {
  const { purchaseAsset } = useContext(BlockchainContext);

  const handlePurchase = async () => {
    try {
      const transactionReceipt = await purchaseAsset(id);
      if (transactionReceipt.status === 'success') {
        alert('Purchase successful!');
      } else {
        alert('Purchase failed.');
      }
    } catch (error) {
      console.error('Purchase error:', error);
      alert('There was an error processing your purchase.');
    }
  };

  return (
    <div className="asset-item">
      <img src={imageUrl} alt={title} className="asset-image" />
      <div className="asset-details">
        <h3 className="asset-title">{title}</h3>
        <p className="asset-description">{description}</p>
        <div className="asset-price">{price} ET</div>
        <button className="asset-purchase-button" onClick={handlePurchase}>
          Purchase
        </button>
      </div>
    </div>
  );
};

export default AssetItem;
import React, { useState, useEffect, useContext } from 'react';
import { BlockchainContext } from '../context/BlockchainContext';
import './dashboard.css';

const CreatorDashboard: React.FC = () => {
  const [assets, setAssets] = useState([]);
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const { getCreatorAssets } = useContext(BlockchainContext);

  const fetchAssets = async () => {
    setIsLoading(true);
    try {
      const fetchedAssets = await getCreatorAssets();
      setAssets(fetchedAssets);
      setError('');
    } catch (err) {
      setError('Failed to fetch assets. Please try again later.');
    }
    setIsLoading(false);
  };

  useEffect(() => {
    fetchAssets();
  }, []);

  return (
    <div className="dashboard-container">
      {isLoading ? (
        <p>Loading assets...</p>
      ) : error ? (
        <p className="error-message">{error}</p>
      ) : (
        assets.map(asset => (
          <div key={asset.id} className="asset">
            {/* Render asset details */}
          </div>
        ))
      )}
    </div>
  );
};

export default CreatorDashboard;

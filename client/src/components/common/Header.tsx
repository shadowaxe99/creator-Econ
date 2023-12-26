```typescript
import React from 'react';
import { Link } from 'react-router-dom';
import { useWallet } from '../../hooks/useWallet';
import './Header.css'; // Assuming a corresponding CSS file for styling

const Header: React.FC = () => {
  const { walletAddress, connectWallet } = useWallet();

  return (
    <header className="header">
      <div className="logo">
        <Link to="/">Elysium Marketplace</Link>
      </div>
      <nav className="navigation">
        <ul>
          <li><Link to="/marketplace">Marketplace</Link></li>
          <li><Link to="/dashboard">Dashboard</Link></li>
        </ul>
      </nav>
      <div className="wallet-info">
        {walletAddress ? (
          <span>{walletAddress}</span>
        ) : (
          <button onClick={connectWallet}>Connect Wallet</button>
        )}
      </div>
    </header>
  );
};

export default Header;
```
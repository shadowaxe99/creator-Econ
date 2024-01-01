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
        <Link to="/" aria-label="Home">Elysium Marketplace</Link>
      </div>
      <nav className="navigation">
        <ul>
          <li><Link to="/marketplace" aria-label="Marketplace">Marketplace</Link></li>
          <li><Link to="/dashboard" aria-label="Dashboard">Dashboard</Link></li>
        </ul>
      </nav>
      <div className="wallet-info">
        {walletAddress ? (
          <span aria-label="Wallet Address">{walletAddress}</span>
        ) : (
          <button onClick={connectWallet} aria-label="Connect Wallet">Connect Wallet</button>
        )}
      </div>
    </header>
  );
};

export default Header;
```
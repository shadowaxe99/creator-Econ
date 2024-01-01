import React from 'react';
import '../styles/globals.css';

const Footer: React.FC = () => {
  return (
    <footer className="footer" role="contentinfo">
      <div className="container">
        <span className="text-muted" aria-label="Copyright Information">© 2023 Elysium Marketplace</span>
      </div>
    </footer>
  );
};

export default Footer;
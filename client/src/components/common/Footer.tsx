import React from 'react';
import '../styles/globals.css';

const Footer: React.FC = () => {
  return (
    <footer className="footer container" role="contentinfo">
      <div>
        <span className="text-muted" aria-label="Copyright 2023 Elysium Marketplace">© 2023 Elysium Marketplace</span>
      </div>
    </footer>
  );
};

export default Footer;
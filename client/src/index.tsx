import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { BlockchainContextProvider } from './context/BlockchainContext';
import './styles/globals.css';

ReactDOM.render(
  <React.StrictMode>
    <BlockchainContextProvider>
      <App />
    </BlockchainContextProvider>
  </React.StrictMode>,
  document.getElementById('root')
);
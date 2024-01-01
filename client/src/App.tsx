import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/common/Header';
import Footer from './components/common/Footer';
import AssetList from './components/marketplace/AssetList';
import CreatorDashboard from './components/dashboard/CreatorDashboard';
import Login from './components/auth/Login';
import SignUp from './components/auth/SignUp';
import BlockchainContextProvider from './context/BlockchainContext';
import './styles/globals.css';

const App: React.FC = () => {
  return (
    <BlockchainContextProvider>
      <Router>
        <div className="App">
          <Header />
          <main>
            <Routes>
              <Route path="/" element={<AssetList />} />
              <Route path="/dashboard" element={<CreatorDashboard />} />
              <Route path="/login" element={<Login />} />
              <Route path="/signup" element={<SignUp />} />
              {/* Additional routes can be added here */}
            </Routes>
          </main>
          <Footer />
        </div>
      </Router>
    </BlockchainContextProvider>
  );
};

export default App;
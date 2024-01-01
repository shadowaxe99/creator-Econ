import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/common/Header';
import Footer from './components/common/Footer';
import AssetList from './components/marketplace/AssetList';
import CreatorDashboard from './components/dashboard/CreatorDashboard';
import Login from './components/auth/Login';
import CreatorDashboard from './components/auth/CreatorDashboard';
import BlockchainContextProvider from './context/BlockchainContext';
import './styles/globals.css';

const App: React.FC = () => {
  return (
    <BlockchainContextProvider>
      <Router>
        <div className="App">
          <Header />
          <main>
            <Switch>
              <Route exact path="/" component={AssetList} />
              <Route path="/dashboard" component={CreatorDashboard} />
              <Route path="/login" component={Login} />
              <Route path="/signup" component={SignUp} />
              {/* Additional routes can be added here */}
            </Switch>
          </main>
          <Footer />
        </div>
      </Router>
    </BlockchainContextProvider>
  );
};

export default App;
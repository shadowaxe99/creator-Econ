import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/common/Header';
import Footer from './components/common/Footer';
import AssetList from './components/marketplace/AssetList';
import CreatorDashboard from './components/dashboard/CreatorDashboard';
import Login from './components/auth/Login';
import SignUp from './components/auth/SignUp';
import BlockchainContextProvider from './context/BlockchainContext';
import './styles/globals.scss'; // Switch to SCSS for more complex styling

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
// Add a loading state to improve UX during data fetching or other asynchronous operations
const [isLoading, setIsLoading] = useState(false);

// Wrap the routes with a loading state check
{isLoading ? <LoadingComponent /> : (
  <Routes>
    <Route path="/" element={<AssetList />} />
    <Route path="/dashboard" element={<CreatorDashboard />} />
    <Route path="/login" element={<Login />} />
    <Route path="/signup" element={<SignUp />} />
    {/* Additional routes can be added here */}
  </Routes>
)}
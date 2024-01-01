import React, { useState, useContext } from 'react';
import { useHistory } from 'react-router-dom';
import { BlockchainContext } from '../context/BlockchainContext';
import './auth.css'; // Assuming a corresponding CSS file for styling

const CreatorDashboard: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const [signUpError, setSignUpError] = useState('');
  const { signUp } = useContext(BlockchainContext);
  const history = useHistory();

  const handleCreatorDashboard = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      setError('Passwords do not match');
      return;
    }
    try {
      await signUp(email, password);
      history.push('/dashboard');
    } catch (error) {
      setSignUpError(error.message || 'An unexpected error occurred. Please try again.');
    }
  };

  return (
    <div className="auth-container">
      <form className="auth-form" onSubmit={handleCreatorDashboard}>
        <h2>Sign Up</h2>
        {signUpError && <div className="error-message">{signUpError}</div>}
        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="confirm-password">Confirm Password</label>
          <input
            type="password"
            id="confirm-password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit" className="auth-submit">Sign Up</button>
      </form>
    </div>
  );
};

export default CreatorDashboard;
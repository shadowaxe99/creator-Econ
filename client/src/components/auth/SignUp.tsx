import React, { useState, useContext } from 'react';
import { useHistory } from 'react-router-dom';
import { BlockchainContext } from '../context/BlockchainContext';
import './auth.css'; // Assuming a corresponding CSS file for styling

const SignUp: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const { signUp } = useContext(BlockchainContext);
  const history = useHistory();

  const handleSignUp = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      setError('Passwords do not match');
      return;
    }
    try {
      await signUp(email, password);
      history.push('/dashboard');
    } catch (error) {
      setError('Failed to create an account');
    }
  };

  return (
    <div className="auth-container">
      <form className="auth-form" onSubmit={handleSignUp}>
        <h2>Sign Up</h2>
        {error && <p className="error">{error}</p>}
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

export default SignUp;
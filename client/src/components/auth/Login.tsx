```typescript
import React, { useState, useContext } from 'react';
import { useHistory } from 'react-router-dom';
import { BlockchainContext } from '../context/BlockchainContext';
import './auth.css'; // Assuming a corresponding CSS file for styling

const Login: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const { login } = useContext(BlockchainContext);
  const history = useHistory();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await login(email, password);
      history.push('/dashboard');
    } catch (error) {
      console.error('Login failed:', error);
      // Handle login error (e.g., show error message to user)
    }
  };

  return (
    <div className="auth-container container">
      <form className="auth-form form-signin mx-auto" onSubmit={handleLogin}>
        <h2>Login</h2>
        <div className="form-group mb-3">
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
        <button type="submit" className="auth-submit btn btn-primary btn-block">Login</button>
      </form>
    </div>
  );
};

export default Login;
```
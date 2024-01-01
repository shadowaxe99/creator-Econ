import { useState, useEffect, useCallback, useContext } from 'react';
import { BlockchainContext } from '../context/BlockchainContext';
import { ethers } from 'ethers';

export const useWallet = () => {
  const [walletAddress, setWalletAddress] = useState<string | null>(null);
  const [balance, setBalance] = useState<string>('0');
  const { provider } = useContext(BlockchainContext);

  const connectWallet = useCallback(async () => {
    if (window.ethereum) {
      try {
        const newAccounts = await window.ethereum.request({
          method: 'eth_requestAccounts',
        });
        setWalletAddress(newAccounts[0]);
      } catch (error) {
        console.error(error);
      }
    } else {
      console.log('Please install MetaMask!');
    }
  }, []);

  const checkWalletConnected = useCallback(async () => {
    if (window.ethereum) {
      try {
        const accounts = await window.ethereum.request({
          method: 'eth_accounts',
        });
        if (accounts.length > 0) {
          setWalletAddress(accounts[0]);
        } else {
          console.log('No accounts found');
        }
      } catch (error) {
        console.error(error);
      }
    }
  }, []);

  const getBalance = useCallback(async () => {
    if (provider && walletAddress) {
      try {
        const balanceBigInt = await provider.getBalance(walletAddress);
        const balanceInEth = ethers.utils.formatEther(balanceBigInt);
        setBalance(balanceInEth);
      } catch (error) {
        console.error('An error occurred while retrieving the wallet balance:', error.message);
      }
    }
  }, [provider, walletAddress, setBalance]);

  useEffect(() => {
    checkWalletConnected();
  }, [checkWalletConnected]);

  useEffect(() => {
    if (walletAddress) {
      getBalance();
    }
  }, [walletAddress, getBalance]);

  return {
    walletAddress,
    balance,
    connectWallet,
  };
};
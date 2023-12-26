// blockchain.ts

import { ethers } from 'ethers';
import { IAsset } from '../interfaces/IAsset';

// Assuming the ABI and contract address are available for the smart contract
import contractABI from './contractABI.json';
const contractAddress = '0x...'; // Replace with actual contract address

export const purchaseAsset = async (assetId: string, buyerAddress: string): Promise<boolean> => {
  try {
    // Initialize Ethereum provider
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    await provider.send('eth_requestAccounts', []); // Request access to wallet
    const signer = provider.getSigner();

    // Connect to the smart contract
    const contract = new ethers.Contract(contractAddress, contractABI, signer);

    // Execute the purchase function from the smart contract
    const transaction = await contract.purchaseAsset(assetId, { from: buyerAddress });
    await transaction.wait(); // Wait for the transaction to be mined

    return true;
  } catch (error) {
    console.error('Error purchasing asset:', error);
    return false;
  }
};

export const fetchAssets = async (): Promise<IAsset[]> => {
  try {
    const provider = new ethers.providers.JsonRpcProvider(); // Connect to Ethereum node
    const contract = new ethers.Contract(contractAddress, contractABI, provider);

    // Call the smart contract to get a list of assets
    const assetsData = await contract.getAssets();
    return assetsData.map((asset: any) => ({
      id: asset.id,
      title: asset.title,
      description: asset.description,
      price: parseFloat(ethers.utils.formatEther(asset.price)),
      imageUrl: asset.imageUrl,
    }));
  } catch (error) {
    console.error('Error fetching assets:', error);
    return [];
  }
};

// Additional blockchain utility functions can be added here as needed.
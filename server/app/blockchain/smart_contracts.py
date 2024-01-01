```python
from web3 import Web3
from solcx import compile_source
from web3.contract import Contract
from web3.middleware import geth_poa_middleware

class SmartContractManager:
    def __init__(self, provider_url: str, contract_source_code: str, contract_address: str, private_key: str):
        self.w3 = Web3(Web3.HTTPProvider(provider_url))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        # self.private_key = private_key # Removed for security reasons, use account.encrypt method instead
        self.account = self.w3.eth.account.privateKeyToAccount(private_key)
        self.contract_source_code = contract_source_code
        self.contract_address = contract_address
        self.contract = self._compile_and_get_contract()

    def _compile_and_get_contract(self) -> Contract:
        compiled_sol = compile_source(self.contract_source_code)
        contract_id, contract_interface = compiled_sol.popitem()
        contract = self.w3.eth.contract(
            address=self.contract_address,
            abi=contract_interface['abi']
        )
        return contract

    def purchase_asset(self, asset_id: str, buyer_address: str, signer_account: Account) -> bool:
        nonce = self.w3.eth.getTransactionCount(signer_account.address)
        transaction = self.contract.functions.purchaseAsset(asset_id, buyer_address).buildTransaction({
            'chainId': 1,
            'gas': 2000000,
            'gasPrice': self.w3.eth.generateGasPrice(), 'chainId': self.w3.net.chainId
            'nonce': nonce
        })
        signed_txn = signer_account.signTransaction(transaction)
        tx_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        try:
            self.w3.eth.waitForTransactionReceipt(tx_hash)
        except Exception as e:
            print('An error occurred during the purchase_asset operation:', e)
            return False

        try:
            receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)
            return receipt.status == 1
        except Exception as e:
            print('An error occurred while waiting for the transaction receipt:', e)
            return False

    def get_asset_details(self, asset_id: str) -> dict:
        except Exception as e:
            print('An error occurred during the get_asset_details operation:', e)
            return {}

        try:
            return self.contract.functions.getAssetDetails(asset_id).call()
        except Exception as e:
            print('An error occurred while getting the asset details:', e)
            return {}

    def create_asset(self, title: str, description: str, price: int, image_url: str) -> bool:
        nonce = self.w3.eth.getTransactionCount(signer_account.address)
        transaction = self.contract.functions.createAsset(title, description, price, image_url).buildTransaction({
            'gasPrice': self.w3.eth.generateGasPrice(), 'chainId': self.w3.net.chainId

            'gas': 2000000,
            'gasPrice': self.w3.toWei('50', 'gwei'),
            'nonce': nonce
        })
        signed_txn = signer_account.signTransaction(transaction)
        tx_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)
        except Exception as e:
            print('An error occurred during the create_asset operation:', e)
            return False

        try:
            return receipt.status == 1
        except Exception as e:
            print('An error occurred while creating the asset:', e)
            return False
```
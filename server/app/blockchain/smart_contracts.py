```python
from web3 import Web3
from solcx import compile_source
from web3.contract import Contract
from web3.middleware import geth_poa_middleware

class SmartContractManager:
    def __init__(self, provider_url: str, contract_source_code: str, contract_address: str, private_key: str):
        self.w3 = Web3(Web3.HTTPProvider(provider_url))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.private_key = private_key
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

    def purchase_asset(self, asset_id: str, buyer_address: str) -> bool:
        nonce = self.w3.eth.getTransactionCount(self.account.address)
        transaction = self.contract.functions.purchaseAsset(asset_id, buyer_address).buildTransaction({
            'chainId': 1,
            'gas': 2000000,
            'gasPrice': self.w3.toWei('50', 'gwei'),
            'nonce': nonce
        })
        signed_txn = self.w3.eth.account.signTransaction(transaction, private_key=self.private_key)
        tx_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)
        return receipt.status == 1

    def get_asset_details(self, asset_id: str) -> dict:
        return self.contract.functions.getAssetDetails(asset_id).call()

    def create_asset(self, title: str, description: str, price: int, image_url: str) -> bool:
        nonce = self.w3.eth.getTransactionCount(self.account.address)
        transaction = self.contract.functions.createAsset(title, description, price, image_url).buildTransaction({
            'chainId': 1,
            'gas': 2000000,
            'gasPrice': self.w3.toWei('50', 'gwei'),
            'nonce': nonce
        })
        signed_txn = self.w3.eth.account.signTransaction(transaction, private_key=self.private_key)
        tx_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)
        return receipt.status == 1
```
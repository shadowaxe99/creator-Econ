```python
# token_management.py
from web3 import Web3
from solcx import compile_source
from .smart_contracts import load_contract

class TokenManager:
    def __init__(self, web3: Web3, contract_address: str, private_key: str):
        self.web3 = web3
        self.contract_address = contract_address
        self.private_key = private_key
        self.contract = load_contract(web3, contract_address)

    def deploy_token_contract(self, contract_source: str, initial_supply: int) -> str:
        compiled_sol = compile_source(contract_source)
        contract_id, contract_interface = compiled_sol.popitem()
        bytecode = contract_interface['bin']
        abi = contract_interface['abi']

        # Create the contract in Python and optimize
        TokenContract = self.web3.eth.contract(abi=abi, bytecode=bytecode)

        # Get the latest transaction
        nonce = self.web3.eth.getTransactionCount(self.web3.eth.defaultAccount)

        # Submit the transaction that deploys the contract
        transaction = TokenContract.constructor(initial_supply).buildTransaction({
            'from': self.web3.eth.defaultAccount,
            'nonce': nonce,
            'gas': 1728712,
            'gasPrice': self.web3.toWei('21', 'gwei')
        })

        # Sign the transaction
        signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)

        # Send the transaction
        tx_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Wait for the transaction to be mined
        tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)

        return tx_receipt.contractAddress

    def transfer_tokens(self, to_address: str, amount: int) -> Any:
        nonce = self.web3.eth.getTransactionCount(self.web3.eth.defaultAccount)
        txn_dict = self.contract.functions.transfer(to_address, amount).buildTransaction({
            'from': self.web3.eth.defaultAccount,
            'nonce': nonce,
            'gas': 2000000,
            'gasPrice': self.web3.toWei('21', 'gwei')
        })

        signed_txn = self.web3.eth.account.sign_transaction(txn_dict, private_key=self.private_key)
        tx_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        return self.web3.eth.waitForTransactionReceipt(tx_hash)

    def get_token_balance(self, address: str) -> int:
        return self.contract.functions.balanceOf(address).call()

# Example usage:
# web3_instance = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
# token_manager = TokenManager(web3_instance, '0xContractAddress', '0xPrivateKey')
# token_manager.deploy_token_contract('contract source code', 1000000)
# token_manager.transfer_tokens('0xRecipientAddress', 100)
# balance = token_manager.get_token_balance('0xAddress')
```
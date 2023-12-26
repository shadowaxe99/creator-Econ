```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///elysium_marketplace.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BLOCKCHAIN_ADDRESS = os.environ.get('BLOCKCHAIN_ADDRESS')
    BLOCKCHAIN_PRIVATE_KEY = os.environ.get('BLOCKCHAIN_PRIVATE_KEY')
    BLOCKCHAIN_NETWORK = os.environ.get('BLOCKCHAIN_NETWORK') or 'http://127.0.0.1:8545'
    ASSET_CONTRACT_ADDRESS = os.environ.get('ASSET_CONTRACT_ADDRESS')
```
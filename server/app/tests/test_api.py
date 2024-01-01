```python
import unittest
from flask import current_app
from app import create_app, db
from app.database.models import Asset
from app.api.routes import api_blueprint
from app.blockchain.smart_contracts import SmartContractManager
from datetime import datetime
from unittest.mock import patch

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.app.register_blueprint(api_blueprint, url_prefix='/api')
        db.create_all()
        self.client = self.app.test_client()

        # Set up mock data
        self.mock_asset = Asset(id='1', title='Mock Asset', description='A mock asset for testing', price=100.0, imageUrl='http://example.com/mock.jpg', is_sold=False)
        db.session.add(self.mock_asset)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_assets(self):
        response = self.client.get('/api/assets')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Mock Asset' in response.get_data(as_text=True))

    def test_purchase_asset(self):
        # Mock the SmartContractManager to always return success
        SmartContractManager.purchase_asset = lambda self, asset_id, buyer_address: True

        response = self.client.post('/api/assets/1/purchase', json={
            'asset_id': '1',
            'buyer_address': '0xMockAddress'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Purchase successful' in response.get_data(as_text=True))

        # Check if the asset is marked as sold
        asset = Asset.query.get('1')
        self.assertTrue(asset.is_sold)

    def test_purchase_nonexistent_asset(self):
        response = self.client.post('/api/assets/999/purchase', json={
            'asset_id': '999',
            'buyer_address': '0xMockAddress'
        })
        self.assertEqual(response.status_code, 404)

    def test_update_asset(self):
        # TODO: Add tests to check the update functionality of the asset

    def test_remove_asset(self):
        # TODO: Add tests to verify the remove (delete) functionality

    def test_purchase_already_sold_asset(self):
        # Mark the asset as sold
        self.mock_asset.is_sold = True
        db.session.commit()

        response = self.client.post('/api/assets/1/purchase', json={
            'asset_id': '1',
            'buyer_address': '0xMockAddress'
        })
        self.assertEqual(response.status_code, 400)
        self.assertTrue('Asset already sold' in response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
```
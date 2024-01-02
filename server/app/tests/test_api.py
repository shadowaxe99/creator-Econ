
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
        # Existing mock and test code

    def test_purchase_asset_invalid_data(self):
        # Test asset purchase with invalid data
        response = self.client.post('/api/assets/1/purchase', json={
            'asset_id': '1',
            'invalid_data': 'InvalidData'
        })
        self.assertEqual(response.status_code, 400)
        self.assertTrue('Invalid purchase data' in response.get_data(as_text=True))
        # Mock the SmartContractManager to always return success
        SmartContractManager.purchase_asset = lambda self, asset_id, buyer_address: True

        response = self.client.post('/api/assets/1/purchase', json={
            'asset_id': '1',
            'buyer_address': '0xMockAddress'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Purchase successful' in response.get_data(as_text=True))

        # Check if the asset is marked as sold in both the database and response data
        asset = Asset.query.get('1')
        self.assertTrue(asset.is_sold)
        self.assertIn('is_sold', response.get_json())

    def test_purchase_nonexistent_asset(self):
        response = self.client.post('/api/assets/999/purchase', json={
            'asset_id': '999',
            'buyer_address': '0xMockAddress'
        })
        self.assertEqual(response.status_code, 404)

<

    def test_purchase_already_sold_asset(self):
        # Existing test code

    def test_get_asset(self):
        # Test fetching a single asset by id
        response = self.client.get('/api/assets/1')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Mock Asset' in response.get_data(as_text=True))

        # Test fetching a non-existent asset by id
        response = self.client.get('/api/assets/999')
        self.assertEqual(response.status_code, 404)
        self.assertTrue('Asset not found' in response.get_data(as_text=True))
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
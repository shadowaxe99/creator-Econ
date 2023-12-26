```python
from flask import Blueprint, jsonify, request
from app.blockchain.smart_contracts import SmartContractManager
from app.database.models import Asset
from app.utils.validators import validate_asset_purchase_data

api_blueprint = Blueprint('api', __name__)
sc_manager = SmartContractManager()

@api_blueprint.route('/assets', methods=['GET'])
def get_assets():
    try:
        assets = Asset.query.filter_by(is_sold=False).all()
        return jsonify([asset.serialize() for asset in assets]), 200
    except Exception as e:
        return jsonify({'message': 'Error fetching assets', 'error': str(e)}), 500

@api_blueprint.route('/assets/<string:asset_id>', methods=['GET'])
def get_asset(asset_id):
    try:
        asset = Asset.query.get_or_404(asset_id)
        return jsonify(asset.serialize()), 200
    except Exception as e:
        return jsonify({'message': 'Asset not found', 'error': str(e)}), 404

@api_blueprint.route('/assets/<string:asset_id>/purchase', methods=['POST'])
def purchase_asset(asset_id):
    try:
        data = request.json
        if not validate_asset_purchase_data(data):
            return jsonify({'message': 'Invalid purchase data'}), 400

        asset = Asset.query.get_or_404(asset_id)
        if asset.is_sold:
            return jsonify({'message': 'Asset already sold'}), 400

        buyer_address = data['buyer_address']
        success, transaction_details = sc_manager.purchase_asset(asset_id, buyer_address)

        if success:
            asset.is_sold = True
            asset.buyer_address = buyer_address
            asset.save()
            return jsonify({
                'message': 'Purchase successful',
                'transaction_details': transaction_details
            }), 200
        else:
            return jsonify({'message': 'Purchase failed', 'details': transaction_details}), 400
    except Exception as e:
        return jsonify({'message': 'Error processing purchase', 'error': str(e)}), 500
```
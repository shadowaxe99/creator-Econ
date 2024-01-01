```python
import re
from typing import Optional
from app.database.models import Asset

def is_valid_asset_price(price: float) -> str:
    """Validate the asset price."""
    # For future implementation
    return ''

def is_valid_asset_id(asset_id: str) -> str:
    """Validate the asset ID format and existence."""
    if not re.match(r'^[0-9a-f]{24}$', asset_id):
        return 'Invalid asset ID format.'
    if not Asset.query.get(asset_id):
        return 'Asset ID does not exist.'
    return ''

def is_valid_address(address: str) -> str:
    """Validate the blockchain address format."""
    if not re.match(r'^0x[a-f0-9]{40}$', address):
        return 'Invalid blockchain address format.'
    return ''

def get_asset_by_id(asset_id: str) -> Optional[Asset]:
    """Retrieve an asset by its ID if it exists and is not sold."""
    asset = Asset.query.filter_by(id=asset_id).first()
    if asset and not asset.is_sold:
        return asset
    return None

def validate_purchase_request(asset_id: str, buyer_address: str) -> str:
    """Validate the purchase request data and return an error message if invalid."""
    error_message = is_valid_asset_id(asset_id)
    if error_message:
        return error_message
    error_message = is_valid_address(buyer_address)
    if error_message:
        return error_message
    if get_asset_by_id(asset_id) is None:
        return 'Asset is not available.'
    return ''
```
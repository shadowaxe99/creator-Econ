```python
import re
from typing import Optional
from app.database.models import Asset

def is_valid_asset_id(asset_id: str) -> bool:
    """Validate the asset ID format."""
    return bool(re.match(r'^[0-9a-fA-F]{24,36}$', asset_id))

def is_valid_address(address: str) -> bool:
    """Validate the blockchain address format."""
    return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address)) and (address == address.lower() or address == address.upper() or address.is_checksum_address(address))

def get_asset_by_id(asset_id: str) -> Optional[Asset]:
    """Retrieve an asset by its ID if it exists and is not sold."""
    asset = Asset.query.filter_by(id=asset_id).first()
    if asset and not asset.is_sold:
        return asset
    return None

def validate_purchase_request(asset_id: str, buyer_address: str) -> bool:
    """Validate the purchase request data."""
    return is_valid_asset_id(asset_id) and is_valid_address(buyer_address) and get_asset_by_id(asset_id) is not None
```
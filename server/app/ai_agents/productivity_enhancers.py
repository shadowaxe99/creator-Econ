```python
# productivity_enhancers.py

from datetime import datetime
from app.database.models import Asset, db
from app.utils.validators import validate_asset_data

class ProductivityEnhancer:
    @staticmethod
    def log_asset_activity(asset_id: str, activity: str):
        """
        Logs activity related to an asset in the database.
        :param asset_id: The ID of the asset.
        :param activity: The activity performed on the asset.
        """
        asset = Asset.query.filter_by(id=asset_id).first()
        if asset:
            asset.last_activity = datetime.utcnow()
            asset.activity_log.append({'timestamp': asset.last_activity, 'activity': activity})
            db.session.commit()

    @staticmethod
    def enhance_asset_data(asset_id: str, new_data: dict):
        """
        Enhances the asset data with additional information.
        :param asset_id: The ID of the asset to enhance.
        :param new_data: A dictionary with the new data to add to the asset.
        """
        asset = Asset.query.filter_by(id=asset_id).first()
        if asset and validate_asset_data(new_data):
            for key, value in new_data.items():
                setattr(asset, key, value)
            db.session.commit()

    @staticmethod
    def generate_activity_report(asset_id: str):
        """
        Generates a report of all activities related to an asset.
        :param asset_id: The ID of the asset.
        :return: A list of activity logs for the asset.
        """
        asset = Asset.query.filter_by(id=asset_id).first()
        if asset:
            return asset.activity_log
        return []

# Example usage:
# ProductivityEnhancer.log_asset_activity('asset_id_123', 'Asset viewed by user')
# ProductivityEnhancer.enhance_asset_data('asset_id_123', {'new_field': 'new_value'})
# report = ProductivityEnhancer.generate_activity_report('asset_id_123')
```
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    assets = db.relationship('Asset', backref=db.backref('owner', lazy='joined', cascade='all, delete-orphan'), lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Asset(db.Model):
    __tablename__ = 'assets'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    image_url = db.Column(db.String(255), nullable=True)
    is_sold = db.Column(db.Boolean, default=False, nullable=False)
    owner_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    def to_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'description': self.description,
            'price': str(self.price),
            'image_url': self.image_url,
            'is_sold': self.is_sold,
            'owner_id': str(self.owner_id)
        }

    def __repr__(self):
        return f'<Asset {self.title}>'

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    asset_id = db.Column(UUID(as_uuid=True), db.ForeignKey('assets.id'), nullable=False)
    buyer_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)
    seller_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    asset = db.relationship('Asset', foreign_keys=[asset_id])
    buyer = db.relationship('User', foreign_keys=[buyer_id])
    seller = db.relationship('User', foreign_keys=[seller_id])

    def to_dict(self):
        return {
            'id': str(self.id),
            'asset_id': str(self.asset_id),
            'buyer_id': str(self.buyer_id),
            'seller_id': str(self.seller_id),
            'price': str(self.price),
            'timestamp': self.timestamp.isoformat()
        }

    def __repr__(self):
        return f'<Transaction {self.id}>'

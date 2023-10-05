from app import db
from flask_login import UserMixin


class UserRole:
    ADMIN = 'admin'
    REGULAR_USER = 'customer'

# Section (Category) Model
class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text)

# Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    manufacture_date = db.Column(db.Date)
    expiry_date = db.Column(db.Date)
    rate_per_unit = db.Column(db.Float)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=False)
    section = db.relationship('Section', backref='products')
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))

# User Model
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default=UserRole.REGULAR_USER)  # 'admin' or 'customer'
    name = db.Column(db.String(255))
    address = db.Column(db.Text)

# Order Model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='orders')
    order_date = db.Column(db.DateTime, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20))  # e.g., 'pending', 'completed', 'shipped'
    delivery_address = db.Column(db.Text)

# Order Item Model (Many-to-Many Relationship)
class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)

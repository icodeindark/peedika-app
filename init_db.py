from app import app, db  # Import 'app' and 'db' objects from 'app/__init__.py'
from app.models import Section, Product, User, Order, OrderItem  # Import your models

with app.app_context():
    db.create_all()
    print("Database tables created successfully.")

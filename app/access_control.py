from functools import wraps
from flask import abort,current_app
from flask_login import current_user
from app.models import UserRole,User
from flask_login import LoginManager








login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    # Load a user by their user_id from your database
    return User.query.get(int(user_id))


def admin_required(view_func):
    @wraps(view_func)
    def decorated_view(*args, **kwargs):
        print(current_user.role)  # Add this line for debugging
        if current_user.role != UserRole.ADMIN:
            abort(403)  # Forbidden
        return view_func(*args, **kwargs)
    return decorated_view

# Custom decorator for regular user access
def regular_user_required(view_func):
    @wraps(view_func)
    def decorated_view(*args, **kwargs):
        if current_user.role != 'customer':
            abort(403)  # Forbidden
        return view_func(*args, **kwargs)
    return decorated_view



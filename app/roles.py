from app import db
from app.models import User, UserRole


def update_user_role():
    # Find the 'topG' user
    user = User.query.filter_by(username='topG').first()

    if user:
        # Update the user's role to 'admin'
        user.role = UserRole.ADMIN

        # Commit the changes to the database
        db.session.commit()
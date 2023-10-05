from app.roles import update_user_role

from app import app,routes,admin_control

from app.access_control import login_manager

login_manager.init_app(app)


if __name__ == '__main__':
    with app.app_context():

        # Call the function to update the user role
        update_user_role()
   


        app.run(debug=True)
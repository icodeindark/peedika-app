from flask import Flask
from flask import render_template, url_for, flash, redirect, request,session
from app import app

from app import app,db
from app.models import Section, Product, User, Order, OrderItem,UserRole
from app.forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash,check_password_hash

from app.access_control import admin_required

from flask_login import login_user






@app.route('/')
def index():
    return render_template('home.html',title='home')

# Define other view functions as needed...
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Define the form here for 'GET' requests
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            # Login successful, you can add user session here if needed.
            login_user(user)  # Log in the user
            print("Logged in as:", user.username)  # Add this line for debugging
            flash('Login successful!', 'success')
            return redirect(url_for('landing_page'))
        else:
            flash('Login unsuccessful. Please check your username and password.', 'danger')

    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove user ID from session
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))


@app.route("/peedika")
def landing_page():
        return render_template('landing_page.html',title='peedika')


@app.route('/peedika/admin', methods=['GET', 'POST'])
@admin_required
def admin_interface():
    if request.method == 'POST':
        # Handle the form submission here
        username_or_email = request.form.get('username_or_email')
        user = User.query.filter_by(username=username_or_email).first()  # Adjust the query as needed

        if user.username == 'topG':
            # Update the user's role or privileges to make them an admin
            user.role = UserRole.ADMIN  # Assuming you have a 'role' field in your User model
            db.session.commit()
            flash(f'{user.username} is now an admin!', 'success')
        else:
            flash('User not found.', 'danger')

    return render_template('admin/dashboard.html',title ='Admin dashboard')

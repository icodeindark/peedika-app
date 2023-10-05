from flask import Flask
from flask import render_template, url_for, flash, redirect, request,session
from app import app

from app import app,db
from app.models import Section, Product, User, Order, OrderItem,UserRole
from app.forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash,check_password_hash

from app.access_control import admin_required

from flask_login import login_user,login_required,current_user



from app.forms import SectionForm, ProductForm

@app.route('/peedika/admin/manage_sections', methods=['GET', 'POST'])
@login_required
def manage_sections():
    section_form = SectionForm()

    if request.method == 'POST':
        section_form = SectionForm()  # Initialize section_form inside the if block

        section_name = request.form.get('section_name')

        # Validate input (e.g., check if section_name is not empty)
        if section_form.validate_on_submit():
            # Create a new section
            new_section = Section(name=section_form.name.data, description=section_form.description.data)

            # Add the new section to the database
            db.session.add(new_section)
            db.session.commit()

            flash('Section added successfully!', 'success')
            return redirect(url_for('manage_sections'))

    # Retrieve all sections from the database
    sections = Section.query.all()

    if current_user.is_authenticated:
        # The user is authenticated, so you can access their role
        role = current_user.role
    else:
        # The user is not authenticated, so they do not have a role
        role = None

    return render_template('admin/manage_sections.html', title='Manage Sections', section_form=section_form, sections=sections, role=role)


@app.route('/peedika/admin/edit_section/<int:id>', methods=['GET', 'POST'])
@admin_required
def edit_section(id):
    section = Section.query.get_or_404(id)

    section_form = SectionForm(obj=section)

    if section_form.validate_on_submit():
        section.name = section_form.name.data
        section.description = section_form.description.data

        db.session.add(section)
        db.session.commit()

        flash('Section updated successfully!', 'success')
        return redirect(url_for('manage_sections'))

    return render_template('admin/edit_section.html', title='Edit Section', section=section, section_form=section_form)

@app.route('/peedika/admin/delete_section/<int:id>', methods=['GET'])
def delete_section(id):
    section = Section.query.get_or_404(id)
    db.session.delete(section)
    db.session.commit()

    flash('Section deleted successfully!', 'success')
    return redirect(url_for('manage_sections'))







@app.route('/peedika/admin/manage_products', methods=['GET', 'POST'])
@admin_required
def manage_products():
    product_form = ProductForm()

    if product_form.validate_on_submit():
        # Create a new product
        new_product = Product(
            name=product_form.name.data,
            manufacture_date=product_form.manufacture_date.data,
            expiry_date=product_form.expiry_date.data,
            rate_per_unit=product_form.rate_per_unit.data,
            section_id=product_form.section_id.data,
            description=product_form.description.data,
            image_url=product_form.image_url.data,
        )
         # Add the new product to the database
        db.session.add(new_product)
        db.session.commit()

        flash('Product added successfully!', 'success')
        return redirect(url_for('manage_products'))
   
    
    
    # Retrieve all products from the database
    products = Product.query.all()


    return render_template('admin/manage_products.html', title='Manage Products', product_form=product_form,products=products)

# You can implement edit and delete functionality here as well.








from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,TextAreaField,DateField, FloatField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length,NumberRange


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')



class SectionForm(FlaskForm):
    name = StringField('Section Name', validators=[DataRequired(), Length(max=255)])
    description = TextAreaField('Description')
    submit = SubmitField('Submit')




class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired(), Length(max=255)])
    manufacture_date = DateField('Manufacture Date')
    expiry_date = DateField('Expiry Date')
    rate_per_unit = FloatField('Rate per Unit', validators=[DataRequired(), NumberRange(min=0)])
    section_id = SelectField('Section', coerce=int, validators=[DataRequired()])
    description = TextAreaField('Description')
    image_url = StringField('Image URL')
    submit = SubmitField('Submit')

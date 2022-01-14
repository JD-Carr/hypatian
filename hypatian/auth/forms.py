"""hypatian.auth.forms."""
from flask_wtf import FlaskForm
from wtforms import (
	BooleanField,
	PasswordField,
	StringField,
	SubmitField
)
from wtforms.validators import (
	DataRequired,
	Email,
	EqualTo,
	Length,
	ValidationError
)
from hypatian.models import User


class LoginForm(FlaskForm):
	"""Declare form for logging in."""

	email = StringField(
		'Email',
		validators=[
			DataRequired(),
			Email(),
			Length(min=8, max=128)
		]
	)
	password = PasswordField(
		'Password',
		validators=[DataRequired()]
	)
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Login')


class LogoutForm(FlaskForm):
	"""Declare form for logging out."""

	submit = SubmitField('Logout')


class RegisterForm(FlaskForm):
	"""Declare form for registering new users."""

	email = StringField(
		'Email',
		validators=[
			DataRequired(),
			Email(),
			Length(min=8, max=128, message='Try a longer/shorter email')
		]
	)
	password = PasswordField(
		'Password',
		validators=[
			DataRequired(),
			Length(min=8, max=128)
		]
	)
	confirm = PasswordField(
		'Confirm Password',
		validators=[
			DataRequired(),
			EqualTo('password')
		]
	)
	submit = SubmitField('Register')

	def validate_email(self, email: str):
		"""Ensure that email is not already in users table.

		:param email: email address to be checked against the ``user`` table
		:type email: str
		"""
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Please use a different email.')

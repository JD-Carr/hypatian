"""hypatian.auth.routes."""
from flask import (
	Blueprint,
	current_app as app,
	flash,
	redirect,
	render_template,
	request,
	session,
	url_for
)
from flask_login import (
	current_user,
	login_required,
	login_user,
	logout_user,
)
from hypatian.auth.forms import (
	LoginForm,
	LogoutForm,
	RegisterForm
)
from hypatian.models.user import User

auth_blueprint = Blueprint(
	'auth',
	__name__,
	template_folder='templates',
	url_prefix='/auth'
)


@auth_blueprint.get('/login')
@auth_blueprint.post('/login')
def login():
	"""Return login form page.

	Prevents already logged-in users from logging in again
	"""
	# If User is already logged in, don't allow them to try to log in again.
	if current_user.is_authenticated:
		app.logger.debug(f'User: {current_user.email} already authenticated, redirecting to profile')
		return redirect(url_for('auth.profile'))

	form = LoginForm()

	if request.method == 'POST' and form.validate_on_submit():
		app.logger.debug('Login form posted and validated')
		email = form.email.data
		password = form.password.data
		remember = form.remember_me.data
		user = User.query.filter_by(email=email).first()

		if user and user.check_password(password):
			session['logged_in'] = True
			user.authenticated = True
			User.update(user)
			login_user(user, remember=remember)
			flash(f'You are logged in as {user}, success')
			app.logger.info(f'User: {user.email} logged in')
			return redirect(url_for('auth.profile'))

		flash("Login failed")
		return redirect(url_for('auth.login'))

	return render_template('auth/login.jinja', form=form)


@auth_blueprint.get('/logout')
@auth_blueprint.post('/logout')
@login_required
def logout():
	"""Logout the current user."""

	session['logged_in'] = False
	user = current_user
	user.authenticated = False
	User.update(user)
	app.logger.info(f'User: {user.email} logged out')
	logout_user()
	return redirect(url_for('main.index', _external=True))


@auth_blueprint.get('/profile')
@auth_blueprint.post('/profile')
@login_required
def profile():
	"""User profile page.

	GET requests serve profile page
	POST requests to log out, to prevent some malicious behaviors
	"""
	form = LogoutForm()

	if request.method == 'POST' and form.validate_on_submit():
		return redirect(url_for('auth.logout'))

	return render_template('auth/profile.jinja', form=form)


@auth_blueprint.get('/register')
@auth_blueprint.post('/register')
def register():
	"""User registration page.

	GET requests serve registration page
	POST requests validate form & add user to user db
	"""
	if current_user.is_anonymous:
		app.logger.debug('User: Anonymous')

	form = RegisterForm()

	if request.method == 'POST' and form.validate_on_submit():
		app.logger.debug('Registration form successfully validated and posted')
		email = form.email.data

		if User.query.filter_by(email=email).first() is None:
			session['logged_in'] = True
			password = form.password.data
			User.create(email=email, password=password)
			new_user = User(email, password)
			login_user(new_user)
			app.logger.info(f'User: {email} registered, redirecting to profile page')
			return redirect(url_for('auth.profile'))

		app.logger.debug('Registration failed')
		flash("Registration failed")
		return redirect(url_for('auth.register'))

	return render_template('auth/register.jinja', form=form)


@auth_blueprint.get('/secret')
@login_required
def secret():
	"""Return a message if user is logged in."""
	return render_template('auth/secret.jinja')

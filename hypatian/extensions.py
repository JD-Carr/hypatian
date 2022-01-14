"""hypatian.extensions.

Declares extensions so they remain importable for factory apps
Declare our extensions before initializing them so they are importable

.. todo:: Look into force_auto_coercion from Flask-SQLAlchemy-Utils
"""
from flask import (
	Flask,
	Response
)
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

__all__ = [
	'bcrypt',
	'db',
	'initialize_extensions',
	'login_manager',
]

bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()


def initialize_extensions(app: Flask) -> None:
	"""Initialize extensions.

	:param app: The Flask instance being passed in to register
	:type app: Flask
	:rtype: None
	"""
	bcrypt.init_app(app)
	app.logger.info('Initialized: Flask-Bcrypt')

	db.init_app(app)

	# Extra safeguard against obliterating prod.
	if app.debug:
		from sqlalchemy import event
		from sqlalchemy.engine import Engine
		from sqlite3 import Connection as SQLite3Connection

		@event.listens_for(Engine, "connect")
		def _set_sqlite_pragma(dbapi_connection, _) -> None:
			"""Ensure foreign keys enforcement is turned on for SQLite databases.

			:param dbapi_connection:
			:type dbapi_connection:
			:rtype: None
			"""
			if isinstance(dbapi_connection, SQLite3Connection):
				isolation_level = dbapi_connection.isolation_level
				dbapi_connection.isolation_level = None
				cursor = dbapi_connection.cursor()
				cursor.execute('PRAGMA foreign_keys = ON')
				cursor.close()
				dbapi_connection.isolation_level = isolation_level
			return None

	app.logger.debug('Initialized: Flask-SQLAlchemy')

	@app.teardown_request
	def teardown_request(response):
		"""Application-wide hook on all request teardowns.

		:param response: The received response
		:type response:
		:returns:
		:rtype:
		"""
		# app.logger.debug('Hook: teardown_request')
		return response

	@app.teardown_appcontext
	def teardown_appcontext(exception=None) -> None:
		"""Close the database connection, everytime the app context tears down.

		A teardown can happen because of two reasons
		1) Everything went well (the error parameter will be None)
		2) an exception happened, in which case the error is passed to the teardown function
		:param exception:
		:type exception:
		:rtype: None
		.. note: http://flask.pocoo.org/docs/0.12/tutorial/dbcon/
		Closes the database again at the end of the request.
		"""
		# app.logger.debug('Hook: teardown_appcontext')
		if exception:
			app.logger.info(f'Hook: {exception}')
		db.session.remove()
		return None

	# Initialize Flask-Login LoginManager
	login_manager.init_app(app)
	login_manager.login_view = 'auth.login'
	login_manager.login_message = app.config['FLASK_LOGIN_MESSAGE']
	login_manager.login_message_category = app.config['FLASK_LOGIN_MESSAGE_CATEGORY']
	login_manager.session_protection = app.config['FLASK_LOGIN_SESSION_PROTECTION']
	app.logger.info('Initialized: Flask-Login')
	return None

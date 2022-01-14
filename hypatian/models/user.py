"""hypatian.models.user.

Creates login user table
"""
from datetime import (
	datetime,
	timedelta
)

from flask import (
	current_app as app,
	redirect,
	url_for
)
from flask_login import (
	UserMixin
)
from sqlalchemy.sql.schema import (
	PrimaryKeyConstraint,
	UniqueConstraint
)
from hypatian.extensions import (
	bcrypt,
	db,
	login_manager
)
from hypatian.mixins import CoreMixin


class User(UserMixin, db.Model, CoreMixin):
	"""Declare user class."""

	__tablename__ = 'user'
	__table_args__ = (
		PrimaryKeyConstraint('id', name='user_pk'),
		UniqueConstraint('email', name='user_email_uk'),
		{
			'schema': 'main',
			'sqlite_autoincrement': True
		}
	)

	id = db.Column(db.Integer(), primary_key=True)
	email = db.Column(db.String(128, collation='NOCASE'), unique=True, index=True, nullable=False)
	password = db.Column(db.String(128), nullable=False)
	active = db.Column(db.Boolean(), nullable=False, server_default=db.true())
	authenticated = db.Column(db.Boolean(), nullable=False, server_default=db.false())
	login_count = db.Column(db.Integer(), nullable=False, server_default="'0'")

	def __init__(self, email: str, password: str) -> None:
		"""Initialize user model."""
		self.email = email
		# Automatically encrypt password upon creation of new user.
		self.password = bcrypt.generate_password_hash(password.encode('UTF-8'))
		app.logger.info(f'User: {self.email} created')

	@classmethod
	def find_by_email(cls, email):
		"""Find user by email address.

		:param email: Target email address
		:type email: str
		:returns:
		:rtype:
		"""
		return cls.query.filter_by(email=email).one_or_none()

	def set_password(self, password: str) -> None:
		"""Set hashed password.

		:param password:
		:type password: str
		:rtype: None
		"""
		self.password = bcrypt.generate_password_hash(self.password, password.encode('UTF-8'))
		return None

	def check_password(self, password: str) -> bool:
		"""Check hashed password.

		:param password: The password to be verified
		:type password: str
		"""
		return bcrypt.check_password_hash(self.password, password.encode('UTF-8'))

	def get_id(self) -> int:
		"""Return the user's `id` to satisfy Flask-Login's requirements.

		:return: id of user
		:rtype: int
		"""
		return self.id

	@property
	def is_active(self) -> bool:
		"""Check if user account is active.

		:return:
		:rtype:
		"""
		return self.active

	@property
	def is_anonymous(self) -> bool:
		"""Return False, as all created users are valid.

		:return:
		:rtype:
		"""
		return False

	@property
	def is_authenticated(self) -> bool:
		"""Return user's current authentication status.

		:return:
		:rtype: bool
		"""
		return self.authenticated

	@property
	def is_new_user(self) -> bool:
		"""Return true if user was created in past 3 days.

		:return:
		:rtype:
		"""
		return self.created_datetime > datetime.utcnow() - timedelta(days=3)


@login_manager.user_loader
def load_user(user_id: int) -> User:
	"""Verify user is authenticated.

	:param user_id: The primary key to search for user in table
	:type user_id: int
	:return:
	:rtype:
	"""
	return User.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized():
	"""Redirect unauthorized users to Login page.

	:return:
	:rtype:
	"""
	return redirect(url_for('auth.login'))

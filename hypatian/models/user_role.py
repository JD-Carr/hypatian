"""hypatian.models.user_role.

Creates user role table
"""
from sqlalchemy.sql.schema import (
	PrimaryKeyConstraint,
	UniqueConstraint
)

from hypatian.extensions import db


class UserRole(db.Model):
	"""Model for user role table."""

	__tablename__ = 'user_role'
	__table_args__ = (
		PrimaryKeyConstraint('user_id', 'role_id', name='user_role_pk'),
		{
			'schema': 'main'
		}
	)

	user_id = db.Column(
		db.Integer(),
		db.ForeignKey('main.user.id', onupdate='CASCADE', ondelete='RESTRICT'),
		index=True,
		primary_key=True,
		nullable=False
	)
	role_id = db.Column(
		db.Integer(),
		db.ForeignKey('main.role.id', onupdate='CASCADE', ondelete='RESTRICT'),
		primary_key=True,
		nullable=False
	)

	# users = db.relationship('User', back_populates='roles', lazy='joined', innerjoin=True)
	# roles = db.relationship('Role', back_populates='users', lazy='joined', innerjoin=True)

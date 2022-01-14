"""hypatian.models.base_table."""
from sqlalchemy.sql.schema import PrimaryKeyConstraint

from hypatian.extensions import db
from hypatian.mixins import CoreMixin


class BaseTable(db.Model, CoreMixin):
	"""Model for base_table table."""

	__tablename__ = 'base_table'
	__table_args__ = (
		PrimaryKeyConstraint('id', name='base_table_pk'),
		{
			'schema': 'main',
			'sqlite_autoincrement': True
		}
	)

	id = db.Column(db.Integer(), primary_key=True)
	col_bool = db.Column(db.Boolean(), nullable=False)
	col_date = db.Column(db.Date(), nullable=False)
	col_datetime = db.Column(db.DateTime, nullable=False)
	col_float = db.Column(db.Float(), nullable=False)
	col_time = db.Column(db.Time(), nullable=False)
	col_varchar = db.Column(db.String(32), nullable=True)

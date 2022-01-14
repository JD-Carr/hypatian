"""hypatian.models.unit_of_measure."""
from sqlalchemy.sql.schema import PrimaryKeyConstraint

from hypatian.extensions import db
from hypatian.mixins import CoreMixin

__all__ = ['UnitOfMeasure']


class UnitOfMeasure(db.Model, CoreMixin):
	"""Declare product data model."""

	__tablename__ = 'unit_of_measure'
	__table_args__ = (
		PrimaryKeyConstraint('id', name='unit_of_measure_pk'),
		{
			'schema': 'main',
			'sqlite_autoincrement': True
		}
	)

	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(64), nullable=False)
	abbreviation = db.Column(db.String(64), nullable=False)
	is_base_unit = db.Column(db.Boolean, nullable=False)

	def __str__(self) -> str:
		"""Return human-friendly string representation of a record.

		:returns: Human-friendly record identifier
		:rtype: str
		"""
		return f'{self.id}'

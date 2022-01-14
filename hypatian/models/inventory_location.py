"""hypatian.model.inventory_location."""
from sqlalchemy.sql.schema import PrimaryKeyConstraint

from hypatian.extensions import db
from hypatian.mixins import CoreMixin

__all__ = ['InventoryLocation']


class InventoryLocation(db.Model, CoreMixin):
	"""Data model for inventory_location table."""

	__tablename__ = 'inventory_location'
	__table_args__ = (
		PrimaryKeyConstraint('id', name='inventory_location_pk'),
		{
			'schema': 'main',
			'sqlite_autoincrement': True
		}
	)

	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(128), nullable=False)

	def __str__(self) -> str:
		"""Return human-friendly string representation of a Inventory Location record.

		:returns: Human-friendly record identifier
		:rtype: str
		"""
		return f'{self.name}'

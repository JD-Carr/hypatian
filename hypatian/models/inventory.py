"""hypatian.model.inventory."""
from sqlalchemy.sql.schema import PrimaryKeyConstraint

from hypatian.extensions import db
from hypatian.mixins import CoreMixin

__all__ = ['Inventory']


class Inventory(db.Model, CoreMixin):
	"""Data model for inventory table."""

	__tablename__ = 'inventory'
	__table_args__ = (
		PrimaryKeyConstraint('id', name='inventory_pk'),
		{
			'schema': 'main',
			'sqlite_autoincrement': True
		}
	)

	id = db.Column(db.Integer(), primary_key=True)
	product_id = db.Column(
		db.Integer(),
		db.ForeignKey('main.product.id', onupdate='CASCADE', ondelete='RESTRICT'),
		nullable=False
	)
	inventory_location_id = db.Column(
		db.Integer(),
		db.ForeignKey('main.inventory_location.id', onupdate='CASCADE', ondelete='RESTRICT'),
		nullable=False
	)
	quantity_in_issue_current = db.Column(db.Integer(), nullable=False)

	def __str__(self) -> str:
		"""Return human-friendly string representation of a Inventory Location record.

		:returns: Human-friendly record identifier
		:rtype: str
		"""
		return f'{self.name}'

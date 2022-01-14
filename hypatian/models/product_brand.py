"""hypatian.models.product_brand."""
from sqlalchemy.sql.schema import PrimaryKeyConstraint

from hypatian.extensions import db
from hypatian.mixins import CoreMixin

__all__ = ['ProductBrand']


class ProductBrand(db.Model, CoreMixin):
	"""Declare product_brand data model."""

	__tablename__ = 'product_brand'
	__table_args__ = (
		PrimaryKeyConstraint('id', name='product_brand_pk'),
		{
			'schema': 'main',
			'sqlite_autoincrement': True
		}
	)

	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(32), nullable=False, unique=True)
	is_active = db.Column(db.Boolean, nullable=False)

	def __str__(self) -> str:
		"""Return human-friendly string representation of a record.

		:return: Human-friendly record identifier
		:rtype: str
		"""
		return f'{self.id}'

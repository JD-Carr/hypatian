"""hypatian.models.product_category."""
from sqlalchemy.sql.schema import PrimaryKeyConstraint

from hypatian.extensions import db
from hypatian.mixins import CoreMixin

__all__ = ['ProductCategory']


class ProductCategory(db.Model, CoreMixin):
	"""Declare product_category data model."""

	__tablename__ = 'product_category'
	__table_args__ = (
		PrimaryKeyConstraint('id', name='product_category_pk'),
		{
			'schema': 'main',
			'sqlite_autoincrement': True
		}
	)

	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(64), nullable=False)
	abbreviation = db.Column(db.String(4), nullable=False)

	products = db.relationship('Product', back_populates='category', lazy='joined')

	def __str__(self) -> str:
		"""Return human-friendly string representation of a record.

		:returns: Human-friendly record identifier
		:rtype: str
		"""
		return f'{self.name}'

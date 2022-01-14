"""hypatian.models.product."""
from sqlalchemy.sql.schema import PrimaryKeyConstraint

from hypatian.extensions import db
from hypatian.mixins import CoreMixin

__all__ = ['Product']


class Product(db.Model, CoreMixin):
	"""Declare product data model."""

	__tablename__ = 'product'
	__table_args__ = (
		PrimaryKeyConstraint('id', name='product_pk'),
		{
			'schema': 'main',
			'sqlite_autoincrement': True
		}
	)

	id = db.Column(db.Integer(), primary_key=True)
	code = db.Column(db.String(25), nullable=False)
	name = db.Column(db.String(64), nullable=False)
	product_brand_id = db.Column(
		db.Integer(),
		db.ForeignKey('main.product_brand.id', onupdate='CASCADE', ondelete='RESTRICT'),
		nullable=False
	)
	product_category_id = db.Column(
		db.Integer(),
		db.ForeignKey('main.product_category.id', onupdate='CASCADE', ondelete='RESTRICT'),
		nullable=False
	)
	purchase_unit_of_measure_id = db.Column(
		db.Integer(),
		db.ForeignKey('main.unit_of_measure.id', onupdate='CASCADE', ondelete='RESTRICT'),
		nullable=False
	)
	issue_unit_of_measure_id = db.Column(
		db.Integer(),
		db.ForeignKey('main.unit_of_measure.id', onupdate='CASCADE', ondelete='RESTRICT'),
		nullable=False
	)
	purchase_unit_to_issue_unit_multiplier = db.Column(db.Integer, nullable=False)
	is_active = db.Column(db.Boolean, nullable=False)

	category = db.relationship('ProductCategory', back_populates='products', lazy='joined')

	def __str__(self) -> str:
		"""Return human-friendly string representation of a record.

		:return: Human-friendly record identifier
		:rtype: str
		"""
		return f'{self.id}'

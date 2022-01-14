"""hypatian.models.product_price."""
from sqlalchemy.sql.schema import PrimaryKeyConstraint

from hypatian.extensions import db
from hypatian.mixins import CoreMixin

__all__ = ['ProductCost']


class ProductCost(db.Model, CoreMixin):
	"""Declare product_price data model."""

	__tablename__ = 'product_cost'
	__table_args__ = (
		PrimaryKeyConstraint('id', name='product_cost_pk'),
		{
			'schema': 'main',
			'sqlite_autoincrement': True
		}
	)

	id = db.Column(db.Integer(), primary_key=True)
	product_id = db.Column(
		db.Integer(),
		db.ForeignKey(
			'main.product.id',
			onupdate='CASCADE',
			ondelete='RESTRICT'
		),
		nullable=False
	)
	cost = db.Column(db.Numeric(precision=10, scale=2, asdecimal=True), nullable=False)
	date_of_cost_start = db.Column(db.DateTime(), nullable=False)
	date_of_cost_end = db.Column(db.DateTime(), nullable=False)
	is_active = db.Column(db.Boolean, nullable=False)

	def __str__(self) -> str:
		"""Return human-friendly string representation of a record.

		:return: Human-friendly record identifier
		:rtype: str
		"""
		return f'{self.id}'

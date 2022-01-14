"""hypatian.model.requisition_order_status."""
from sqlalchemy.sql.schema import PrimaryKeyConstraint

from hypatian.extensions import db
from hypatian.mixins import CoreMixin

__all__ = ['RequisitionOrderStatus']


class RequisitionOrderStatus(db.Model, CoreMixin):
	"""Data model for requisition_order_status table."""

	__tablename__ = 'requisition_order_status'
	__table_args__ = (
		PrimaryKeyConstraint('id', name='requisition_order_status_pk'),
		{
			'schema': 'main',
			'sqlite_autoincrement': True
		}
	)

	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(128), nullable=False)

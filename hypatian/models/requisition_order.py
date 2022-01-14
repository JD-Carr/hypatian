"""hypatian.model.requisition_order."""
from sqlalchemy.sql.schema import PrimaryKeyConstraint

from hypatian.extensions import db
from hypatian.mixins import CoreMixin

__all__ = ['RequisitionOrder']


class RequisitionOrder(db.Model, CoreMixin):
	"""Data model for requisition_order table."""

	__tablename__ = 'requisition_order'
	__table_args__ = (
		PrimaryKeyConstraint('id', name='requisition_order_pk'),
		{
			'schema': 'main',
			'sqlite_autoincrement': True
		}
	)

	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(128), nullable=False)
	stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=False)
	original_quantity = db.Column(db.Integer, nullable=False)
	qty = db.Column(db.Integer, nullable=False)
	date_applied = db.Column(db.DateTime, nullable=False)
	status = db.Column(db.Integer, default=0)
	accepted = db.Column(db.Boolean, default=False)
	admins_comment = db.Column(db.Text, nullable=False, default="No Comments")
	users_comment = db.Column(db.Text, nullable=False)
	received_comment = db.Column(db.Text, default="No Comments")
	processed_by = db.Column(db.String(255), nullable=False, default='Not yet Processed')

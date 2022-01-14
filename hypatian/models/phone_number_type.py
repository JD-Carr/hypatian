"""hypatian.models.phone_number_type."""
from sqlalchemy.sql.schema import PrimaryKeyConstraint

from hypatian.extensions import db

__all__ = ['PhoneNumberType']


class PhoneNumberType(db.Model):
	"""Model for phone_number_type table.

	Child of patient_phone_number
	"""

	__tablename__ = 'phone_number_type'
	__table_args__ = (
		PrimaryKeyConstraint('id', name='phone_number_type_pk'),
		{
			'schema': 'main',
			'sqlite_autoincrement': True
		}
	)

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(25), nullable=False)

	patient_phone_numbers = db.relationship('PatientPhoneNumber', back_populates='phone_number_type', lazy='joined')

	def __str__(self) -> str:
		"""Return human-friendly string representation of a Phone Number Type record.

		:returns: Human-friendly record identifier
		:rtype: str
		"""
		return f'{self.name}'

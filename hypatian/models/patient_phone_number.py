"""hypatian.models.patient_phone_number."""
from sqlalchemy.sql.schema import PrimaryKeyConstraint

from hypatian.extensions import db

__all__ = ['PatientPhoneNumber']


class PatientPhoneNumber(db.Model):
	"""Data model patient phone numbers."""

	__tablename__ = 'patient_phone_number'
	__table_args__ = (
		PrimaryKeyConstraint('id', name='patient_phone_number_pk'),
		{
			'schema': 'main',
			'sqlite_autoincrement': True
		}
	)

	id = db.Column(db.Integer(), primary_key=True)
	patient_id = db.Column(db.Integer(), db.ForeignKey(
		'main.patient.id', onupdate='CASCADE', ondelete='RESTRICT'), nullable=False)
	phone_number = db.Column(db.String(15), nullable=False)
	phone_number_type_id = db.Column(db.Integer(), db.ForeignKey(
		'main.phone_number_type.id', onupdate='CASCADE', ondelete='RESTRICT'), nullable=False, server_default="'1'")
	extension = db.Column(db.String(4), nullable=False, server_default='')
	is_current = db.Column(db.Boolean(), nullable=False, server_default=db.true())

	patient = db.relationship('Patient', back_populates='phone_numbers', lazy='joined', innerjoin=True)
	phone_number_type = db.relationship(
		'PhoneNumberType', back_populates='patient_phone_numbers', lazy='joined', innerjoin=True)

	def __str__(self) -> str:
		"""Return human-friendly string representation of a Patient Phone Number record.

		:returns: Human-friendly record identifier
		:rtype: str
		"""
		return f'{self.phone_number}'

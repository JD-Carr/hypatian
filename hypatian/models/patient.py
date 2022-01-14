"""Model for patient table."""
from datetime import date

from sqlalchemy.sql.schema import PrimaryKeyConstraint

from hypatian.extensions import db
from hypatian.mixins import CoreMixin
from hypatian.models.utils import SQLITE_NOW


class Patient(db.Model, CoreMixin):
	"""Declare patient data model."""

	__tablename__ = 'patient'
	__table_args__ = (
		PrimaryKeyConstraint('id', name='patient_pk'),
		{
			'schema': 'main',
			'sqlite_autoincrement': True
		}
	)

	id = db.Column(db.Integer(), primary_key=True)
	name_last = db.Column(db.String(50), nullable=False)
	name_first = db.Column(db.String(50), nullable=False)
	name_preferred = db.Column(db.String(50), nullable=True, server_default='')
	name_middle = db.Column(db.String(50), nullable=True, server_default='')
	date_of_birth = db.Column(db.Date(), nullable=False)
	date_of_death = db.Column(db.Date(), nullable=True)
	is_deceased = db.Column(db.Boolean, nullable=False, server_default=db.false())
	created_datetime = db.Column(db.DateTime(), nullable=False, server_default=db.text(SQLITE_NOW))
	created_user = db.Column(db.String(64), nullable=False, server_default='automata')
	modified_datetime = db.Column(db.DateTime(), nullable=False, server_default=db.text(SQLITE_NOW))
	modified_user = db.Column(db.String(64), nullable=False, server_default='automata')

	phone_numbers = db.relationship('PatientPhoneNumber', back_populates='patient', lazy='joined')

	@property
	def age(self) -> int:
		"""Return patient age.

		:return:
		:rtype: int
		"""
		today = date.today()
		return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

	@property
	def name_full(self) -> str:
		"""Return the first + last name of patient.

		:return: Human-friendly string of record
		:rtype: str
		"""
		return f'{self.name_first} {self.name_last}'

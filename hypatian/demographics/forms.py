"""hypatian.demographics.forms."""
from flask_wtf import FlaskForm
from wtforms import (
	DateField,
	StringField,
	SubmitField
)
from wtforms.validators import (
	DataRequired,
	Length,
	Optional
)

__all__ = ['PatientEntryForm']


class PatientEntryForm(FlaskForm):
	"""Form for creating a new patient record."""

	name_first = StringField(
		'First Name',
		validators=[
			DataRequired(message='Please enter first name'),
			Length(min=1, max=64)
		]
	)

	name_preferred = StringField(
		'Preferred Name',
		validators=[
			Length(max=64),
			Optional()
		]
	)

	name_middle = StringField(
		'Middle Name',
		validators=[
			Length(max=64),
			Optional()
		]
	)

	name_last = StringField(
		'Last Name',
		validators=[
			DataRequired(message='Please enter last name'),
			Length(min=1, max=64)
		]
	)

	date_of_birth = DateField(
		'Date of Birth',
		format='%Y-%m-%d',
		validators=[
			DataRequired(message='Please enter date of birth')
		]
	)

	submit = SubmitField('Submit')

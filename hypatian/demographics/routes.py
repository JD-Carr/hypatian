"""hypatian.demographics.routes."""
from flask import (
	Blueprint,
	current_app as app,
	render_template
)
from hypatian.demographics.forms import PatientEntryForm

__all__ = ['demographics_blueprint']

demographics_blueprint = Blueprint(
	'demographics',
	__name__,
	template_folder='templates',
	url_prefix='/demographics'
)


@demographics_blueprint.post('/patient-entry')
@demographics_blueprint.get('/patient-entry')
def patient_entry():
	"""Return new patient entry form."""
	app.logger.debug('Patient entry page reached')

	form = PatientEntryForm()
	return render_template('demographics/patient_entry.jinja', form=form)


@demographics_blueprint.get('/patient-details/<int:patient_id>')
def patient_details(patient_id: int):
	"""Return new patient view page."""
	_id = str(patient_id)
	app.logger.debug('patient detail view reached')
	return render_template('demographics/patient_details.jinja', patient_id=_id)


@demographics_blueprint.get('/patients')
def patients():
	"""Return page with all patient records."""
	return render_template('demographics/patients.jinja')


@demographics_blueprint.get('/patient-card')
def patient_card():
	"""Return page with all patient records."""
	return render_template('demographics/patient_card.jinja')

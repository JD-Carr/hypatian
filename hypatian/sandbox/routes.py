"""hypatian.sandbox.routes."""
from flask import (
	Blueprint,
	current_app as app,
	flash,
	jsonify,
	make_response,
	redirect,
	render_template,
	request,
	session,
	url_for
)

sandbox_blueprint = Blueprint(
	'sandbox',
	__name__,
	template_folder='templates',
	url_prefix='/sandbox'
)


@sandbox_blueprint.get('/patient-details/<int:patient_id>')
def patient_details(patient_id: int):
	"""Return new patient view page.

	:param patient_id: primary key for patient record
	:type patient_id: int
	"""
	app.logger.debug(f'patient {patient_id} detail view reached')
	return render_template('sandbox/patient_details.jinja', patient_id=patient_id)


@sandbox_blueprint.get('/patients')
def patients():
	"""Return all patient records."""
	return render_template('sandbox/patients.jinja')


@sandbox_blueprint.get('/patients-axios')
def patients_axios():
	"""Return all patient records."""
	return render_template('sandbox/patients_axios.jinja')


@sandbox_blueprint.get('/simple/<int:patient_id>')
def simple(patient_id: int):
	"""Return a simple page."""
	return render_template('sandbox/simple.jinja', patient_id=patient_id)

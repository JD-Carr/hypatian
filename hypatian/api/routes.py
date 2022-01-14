"""hypatian.api.routes."""
from flask import (
	Blueprint,
	Response,
	current_app as app,
	jsonify,
	make_response,
	request
)
from hypatian.models import (
	Patient,
	User
)
from hypatian.utils import (
	get_date_format,
	now
)

api_blueprint = Blueprint(
	'api',
	__name__,
	template_folder='templates',
	url_prefix='/api'
)


@api_blueprint.get('/patients')
@api_blueprint.post('/patients')
@api_blueprint.get('/patients/<int:patient_id>')
@api_blueprint.patch('/patients/<int:patient_id>')
@api_blueprint.delete('/patients/<int:patient_id>')
def patients(patient_id=None) -> Response:
	"""Get single patient record by ``patient_id``.

	.. note:: Work on this

	:param patient_id: The primary key for the patient table
	:type patient_id: int
	:return:
	:rtype: Response
	"""
	if patient_id and Patient.query.get(patient_id) is None:
		message = jsonify({'error': 'Resource Not Found', 'status': 404})
		response = make_response(message, 404)
		return response

	if request.method == 'GET':
		if patient_id:
			patient = [Patient.query.get(patient_id).to_dict()]
			message = jsonify({'data': patient})

		else:
			_patients = {"data": [patient.to_dict() for patient in Patient.query.all()]}
			message = jsonify({'data': _patients})

		response = make_response(message, 200)
		return response

	if request.method == 'DELETE':
		patient = Patient.query.get(patient_id)
		patient.delete()
		message = jsonify({'message': 'OK'})
		response = make_response(message, 204)
		return response

	if request.is_json:
		if request.method == 'POST':
			data = request.get_json()
			data['date_of_birth'] = get_date_format(data['date_of_birth'])
			app.logger.debug(f'POST <patient: {data}>')
			Patient.create(**data)
			message = jsonify({'message': 'OK'})
			response = make_response(message, 201)
			return response

		if request.method == 'PATCH':
			data = request.get_json()
			app.logger.debug(f'PATCH <patient: {data}>')
			patient = Patient.query.get(patient_id)
			patient.delete()
			message = jsonify({'message': 'OK'})
			response = make_response(message, 204)
			return response

	data = jsonify({'error': 'No JSON recevied'})
	response = make_response(data, 400)
	return response


@api_blueprint.get('/users')
@api_blueprint.post('/users')
@api_blueprint.get('/users/<int:patient_id>')
@api_blueprint.patch('/users/<int:patient_id>')
@api_blueprint.delete('/users/<int:patient_id>')
def users(user_id=None) -> Response:
	"""Get single patient record by ``patient_id``.

	:param patient_id: The primary key for the patient table
	:type patient_id: int
	:return:
	:rtype: Response
	"""
	if user_id and User.query.get(user_id) is None:
		message = jsonify({'error': 'Resource Not Found', 'status': 404})
		response = make_response(message, 404)
		return response

	if request.method == 'GET':
		if user_id:
			payload = [Patient.query.get(user_id).to_dict()]
			message = jsonify({'data': payload})

		else:
			payload = {"data": [user.to_dict() for user in User.query.all()]}
			message = jsonify({'data': payload})

		response = make_response(message, 200)
		return response

	if request.method == 'DELETE':
		payload = User.query.get(user_id)
		payload.delete()
		message = jsonify({'message': 'OK'})
		response = make_response(message, 204)
		return response

	if request.is_json:
		if request.method == 'POST':
			payload = request.get_json()
			payload['date_of_birth'] = get_date_format(payload['date_of_birth'])
			app.logger.debug(f'POST <patient: {payload}>')
			User.create(**payload)
			message = jsonify({'message': 'OK'})
			response = make_response(message, 201)
			return response

		if request.method == 'PATCH':
			payload = request.get_json()
			app.logger.debug(f'PATCH <patient: {payload}>')
			user = User.query.get(user_id)
			user.delete()
			message = jsonify({'message': 'OK'})
			response = make_response(message, 204)
			return response

	message = jsonify({'error': 'No JSON recevied'})
	response = make_response(message, 400)
	return response


@api_blueprint.after_request
def default_headers(response) -> Response:
	"""Add default headers to all return respones."""
	response.headers['Content-Type'] = 'application/json'
	response.mimetype = 'application/json'
	response.now = now()
	return response

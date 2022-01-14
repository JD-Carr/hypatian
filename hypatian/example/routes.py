"""hypatian.example.routes."""
from flask import (
	Blueprint,
	Markup,
	Response,
	abort,
	current_app as app,
	flash,
	jsonify,
	make_response,
	render_template,
	request
)
from hypatian.utils import now

example_blueprint = Blueprint(
	'example',
	__name__,
	url_prefix='/example'
)


@example_blueprint.get('/abort/<int:code>')
def abort_endpoint(code: int):
	"""Test errors.

	Endpoint used to abort whichever code we want (typically 400 >= code <= 500)
	:param code: Send any http error code
	:type code: int
	"""
	abort(code)


@example_blueprint.get('/item/')
@example_blueprint.get('/item/<int:item_id>')
def item_get(item_id=None):
	"""Prototype of."""
	if not item_id:
		message = jsonify(message='"item_id" missing')
		response = make_response(message, 400)
		return response

	message = jsonify(item_id=item_id, color='blue')
	return make_response(message, 200)


@example_blueprint.route('/date/<int:year>/')
@example_blueprint.route('/date/<int:year>/<int:month>/')
@example_blueprint.route('/date/<int:year>/<int:month>/<int:day>/')
def date_get(year=None, month=None, day=None):
	"""Prototype of request."""
	message = (f'{year}{month}{day}')
	response = make_response(message, 200)
	return response


@app.route('/flash', methods=['GET', 'POST'])
def test_flash():
	"""Test flash messages."""
	flash('A simple default alert—check it out!')
	flash('A simple primary alert—check it out!', 'primary')
	flash('A simple secondary alert—check it out!', 'secondary')
	flash('A simple success alert—check it out!', 'success')
	flash('A simple danger alert—check it out!', 'danger')
	flash('A simple warning alert—check it out!', 'warning')
	flash('A simple info alert—check it out!', 'info')
	flash('A simple light alert—check it out!', 'light')
	flash('A simple dark alert—check it out!', 'dark')
	flash(Markup('A simple success alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.'), 'success')
	return render_template('flash.html')


@example_blueprint.before_app_first_request
def before_app_first_request() -> None:
	"""Run only before the first requests made."""
	app.logger.debug('Hook: before_app_first_request')
	return None


@example_blueprint.before_request
def before_request() -> None:
	"""Run before each requests."""
	app.logger.debug('Hook: before_request')
	return None


@example_blueprint.after_request
def default_headers(response) -> Response:
	"""Add headers to all return respones."""
	app.logger.debug('Hook: after_request')
	return response

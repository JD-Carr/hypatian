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

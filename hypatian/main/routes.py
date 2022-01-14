"""hypatian.main.routes."""
from flask import (
	Blueprint,
	Response,
	current_app as app,
	jsonify,
	make_response,
	render_template,
	request,
	send_from_directory
)
from hypatian.utils import now

main_blueprint = Blueprint(
	'main',
	__name__,
	url_prefix='/',
	template_folder='templates',
	static_folder='static',
	static_url_path='/static'
)


@main_blueprint.get('/')
@main_blueprint.get('/index')
def index():
	"""Return the status of the server if it's still running."""
	return render_template('index.jinja')


@main_blueprint.get('/cfg')
def cfg():
	"""Return important config settings."""
	message = jsonify(
		environment=app.config['ENV'],
		debug=app.config['DEBUG'],
		testing=app.config['TESTING'],
		secure=app.config['SECURE'],
		jsonify_prettyprint_regular=app.config['JSONIFY_PRETTYPRINT_REGULAR'],
		preferred_url_scheme=app.config['PREFERRED_URL_SCHEME'],
		session_cookie_secure=app.config['SESSION_COOKIE_SECURE'],
		use_x_sendfile=app.config['USE_X_SENDFILE'],
		apache_server_name=app.config['APACHE_SERVER_NAME'],
		apache_run_user=app.config['APACHE_RUN_USER'],
		apache_run_group=app.config['APACHE_RUN_GROUP'],
		apache_log_dir=app.config['APACHE_LOG_DIR'],
		apache_run_dir=app.config['APACHE_RUN_DIR'],
		apache_lock_dir=app.config['APACHE_LOCK_DIR'],
		apache_vhosts_dir=app.config['APACHE_VHOSTS_DIR'],
		apache_ssl_scache=app.config['APACHE_SSL_SCACHE'],
		apache_pid_file=app.config['APACHE_PID_FILE']
	)
	response = make_response(message, 200)
	response.mimetype = 'application/json'
	return response


@main_blueprint.get('/deny')
def deny():
	"""Return page denied by robots.txt rules.

	tags: Response formats
	produces: text/plain
	responses: 200:
	description: Denied message
	"""
	response = make_response()
	response.data = 'NO'
	response.content_type = 'text/plain'
	return response


@main_blueprint.get('/item/')
@main_blueprint.get('/item/<int:item_id>')
def item(item_id=None):
	"""Prototype a basic get record route.

	:param item_id: Primary key for item
	:type item_id: int
	"""
	if not item_id:
		message = jsonify(message='"item_id" missing')
		response = make_response(message, 400)
		response.mimetype = 'application/json'
		return response

	message = jsonify(id=item_id, color='Blue', in_stock=True)
	response = make_response(message, 200)
	response.mimetype = 'application/json'
	return response


@main_blueprint.get('/robots.txt')
def robots():
	"""Return robot text.

	.. note:: If this doesn't work, check apache and environment variables
	:return: robot.txt
	"""
	return send_from_directory(app.static_folder, request.path[1:])


@main_blueprint.get('/health')
def health():
	"""Return the status of the server if it's still running.

	.. todo:: This should actually perform some greater diagnostic check
	"""
	message = jsonify(message='OK')
	response = make_response(message, 200)
	response.mimetype = 'application/json'
	response.headers['Content-Type'] = 'application/health+json'
	return response


@main_blueprint.after_request
def default_headers(response):
	"""Add headers to all return respones."""
	response.headers['Last-Modified'] = now()
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Cache-Control'] = 'Fri, 31 Jan 2020 00:00:00 GMT'
	return response

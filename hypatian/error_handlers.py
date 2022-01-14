"""error_handlers."""
from flask import (
	Flask,
	render_template
)

__all__ = ['register_error_handlers']


def register_error_handlers(app: Flask):
	"""Register all HTTP error handlers.

	All error handlers
	"""

	def handle_client_error_page(err, status):
		"""Render all client HTTP error pages.

		This is the general client HTTP error handler.
		:param Error err: error message.
		:param Status status: the status code.
		"""
		app.logger.debug(f'<error: {err}> <status: {status}>')
		return render_template('error.jinja', error=err, status=status), status

	def handle_server_error_page(err, status):
		"""Render all server HTTP error pages.

		This is the general server HTTP error handler.
		:param Error err: error message.
		:param Status status: the status code.
		"""
		app.logger.debug(f'<error: {err}> <status: {status}>')
		return render_template('error.jinja', error=err, status=status), status

	@app.errorhandler(400)
	def bad_request(err):
		"""Error 400: Bad Request."""
		return handle_client_error_page(err, status=400)

	@app.errorhandler(401)
	def unauthorized(err):
		"""Error 401: Unauthorized."""
		return handle_client_error_page(err, status=401)

	def payment_required(err):
		"""Error 402: Payment Required."""
		return handle_client_error_page(err, status=402)

	@app.errorhandler(403)
	def forbidden(err):
		"""Error 403: Forbidden."""
		return handle_client_error_page(err, status=403)

	@app.errorhandler(404)
	def not_found(err):
		"""Error 404: Not Found."""
		return handle_client_error_page(err, status=404)

	@app.errorhandler(405)
	def method_not_allowed(err):
		"""Error 405: Method Not Allowed."""
		return handle_client_error_page(err, status=405)

	@app.errorhandler(406)
	def not_acceptable(err):
		"""Error 406: Not Acceptable."""
		return handle_client_error_page(err, status=406)

	def proxy_authentication_required(err):
		"""Error 407: Proxy Authentication Required."""
		return handle_client_error_page(err, status=407)

	@app.errorhandler(408)
	def request_timeout(err):
		"""Error 408: Request Timeout."""
		return handle_client_error_page(err, status=408)

	@app.errorhandler(409)
	def conflict(err):
		"""Error 409: Conflict."""
		return handle_client_error_page(err, status=409)

	@app.errorhandler(410)
	def gone(err):
		"""Error 410: Gone."""
		return handle_client_error_page(err, status=410)

	@app.errorhandler(411)
	def length_required(err):
		"""Error 411: Length Required."""
		return handle_client_error_page(err, status=411)

	@app.errorhandler(412)
	def precondition_failed(err):
		"""Error 412: Precondition Failed."""
		return handle_client_error_page(err, status=412)

	@app.errorhandler(413)
	def payload_too_large(err):
		"""Error 413: Payload Too Large."""
		return handle_client_error_page(err, status=413)

	@app.errorhandler(414)
	def uri_too_long(err):
		"""Error 414: URI Too Long."""
		return handle_client_error_page(err, status=414)

	@app.errorhandler(415)
	def unsupported_media_type(err):
		"""Error 415: Unsupported Media Type."""
		return handle_client_error_page(err, status=415)

	@app.errorhandler(416)
	def range_not_satisfiable(err):
		"""Error 416: Range Not Satisfiable."""
		return handle_client_error_page(err, status=416)

	@app.errorhandler(417)
	def expectation_failed(err):
		"""Error 417: Expectation Failed."""
		return handle_client_error_page(err, status=417)

	@app.errorhandler(429)
	def too_many_requests(err):
		"""Error 429: Too Many Requests."""
		return handle_client_error_page(err, status=429)

	@app.errorhandler(500)
	def internal_server_error(err):
		"""500 - Internal Server Error."""
		return handle_server_error_page(err, status=500)

	app.logger.info('Registered: Error Handlers')

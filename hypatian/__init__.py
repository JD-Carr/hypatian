"""hypatian."""
from flask import Flask

__all__ = ['create_app']
__version__ = '1.0.0'


def create_app() -> Flask:
	"""Create app using factory methodology.

	:return: The Flask app as an object
	:rtype: Flask
	"""
	app = Flask(__name__)

	app.config.from_pyfile('config.py')

	with app.app_context():
		from hypatian.loggers import configure_logging
		configure_logging(app)

		from hypatian.blueprints import register_blueprints
		register_blueprints(app)

		from hypatian.extensions import initialize_extensions
		initialize_extensions(app)

		from hypatian.jinja import configure_jinja
		configure_jinja(app)

		from hypatian.commands import register_commands
		register_commands(app)

		# Configure error handlers, if in production.
		# For testing the error handlers themselves, will need to change this code.
		# TODO: Look into a possible config setting for more nuanced testing.
		if not app.debug:
			from hypatian.error_handlers import register_error_handlers
			register_error_handlers(app)

	return app

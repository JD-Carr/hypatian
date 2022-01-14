"""hypatian.blueprints."""
from flask import Flask

__all__ = ['register_blueprints']


def register_blueprints(app: Flask) -> None:
	"""Register routes used by the app.

	:param app: The app
	:type app: Flask
	:rtype: None
	"""
	from hypatian.api import api_blueprint
	app.register_blueprint(api_blueprint)
	app.logger.info('Registered: Blueprint - API')

	from hypatian.auth import auth_blueprint
	app.register_blueprint(auth_blueprint)
	app.logger.info('Registered: Blueprint - Auth')

	from hypatian.demographics import demographics_blueprint
	app.register_blueprint(demographics_blueprint)
	app.logger.info('Registered: Blueprint - Demographics')

	from hypatian.main import main_blueprint
	app.register_blueprint(main_blueprint)
	app.logger.info('Registered: Blueprint - Main')
	return None

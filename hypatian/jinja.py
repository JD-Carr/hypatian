"""hypatian.jinja."""
from flask import Flask

__all__ = ['configure_jinja']


def configure_jinja(app: Flask) -> None:
	"""Configure jinja environment.

	:param app:
	:type app: Flask
	:rtype: None
	"""
	# By default Jinja2 strips tailing newline from the rendered template
	# These force the resulting file to match the tempalte exactly for replacement files
	app.jinja_env.keep_trailing_newline = True
	app.jinja_env.lstrip_blocks = True
	app.jinja_env.trim_blocks = True

	# The following causes `None` to be rendered in templates as "" instead of `None`
	app.jinja_env.finalize = lambda x: '' if x is None else x

	app.jinja_env.autoescape = True

	# Custom global settings
	app.jinja_env.globals['APP_NAME'] = app.config['APP_NAME']
	app.jinja_env.globals['ENV'] = app.config['ENV']

	app.logger.info('Configured: Jinja')
	return None

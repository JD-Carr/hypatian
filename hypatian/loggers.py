"""hypatian.loggers.

Declare the logging configurations for the app
Not fond of using configfile formats by python
Setting logs programmatically I find more flexible and easier to adjust given how the project relies on environment
variables whic are easy to change in the container as needed.
Programmatically configured is about the same code verbosity
Flask will add a StreamHandler (default_handler) to hypatian.logger automatically
During requests, it will write to the stream specified by the WSGI server in environ['wsgi.errors']
(which is usually sys.stderr)
Outside a request, it will log to sys.stderr
"""
import datetime
from datetime import timezone
import logging
import logging.handlers
from sys import (
	stderr,
	stdout
)
from flask import Flask
from flask.logging import (
	default_handler,
	wsgi_errors_stream
)

__all__ = ['configure_logging']


class InfoFilter(logging.Filter):
	"""Filter out messages that are not info.

	Used to keep info messages tracked in a separate log during production.
	info messages should be tailored for metrics or auditing.
	"""

	def __init__(self):
		logging.Filter.__init__(self)

	def filter(self, record):
		return record.levelno == logging.INFO


def configure_logging(app: Flask) -> None:
	"""Configure log settings for the app.

	:param app:
	:type app: Flask
	:rtype: None
	"""
	env = app.config['ENV']
	debug = app.debug
	secure = app.config['SECURE']
	log_dir = app.config['APP_LOG_DIR']
	log_file_app = log_dir / 'app.log'
	log_file_db = log_dir / 'db.log'
	log_file_werkzeug = log_dir / 'werkzeug.log'
	log_level = logging.DEBUG if debug else logging.WARNING

	# Remove existing handlers so we don't duplicate logging.
	app.logger.removeHandler(default_handler)
	for handler in logging.getLogger('werkzeug').handlers:
		logging.getLogger('werkzeug').removeHandler(handler)
		handler.close()
	for handler in logging.getLogger('sqlalchemy').handlers:
		logging.getLogger('sqlalchemy').removeHandler(handler)
		handler.close()
	for handler in logging.getLogger('sqlalchemy.engine').handlers:
		logging.getLogger('sqlalchemy.engine').removeHandler(handler)
		handler.close()
	for handler in logging.getLogger('sqlalchemy.dialects').handlers:
		logging.getLogger('sqlalchemy.dialects').removeHandler(handler)
		handler.close()
	for handler in logging.getLogger('sqlalchemy.orm').handlers:
		logging.getLogger('sqlalchemy.orm').removeHandler(handler)
		handler.close()
	for handler in logging.getLogger('sqlalchemy.pool').handlers:
		logging.getLogger('sqlalchemy.pool').removeHandler(handler)
		handler.close()

	fmt_short = logging.Formatter(
		fmt='[%(levelname)-8s] [%(name)s] %(module)s.%(funcName)s():%(lineno)-4s %(message)s',
		datefmt='%Y-%m-%d %H:%M:%S'
	)

	fmt_long = logging.Formatter(
		fmt='%(asctime)s [%(levelname)-8s] [%(name)s] %(module)s.%(funcName)s():%(lineno)-4s %(message)s',
		datefmt='%Y-%m-%d %H:%M:%S'
	)

	midnight = datetime.time(hour=0, minute=0, second=0, tzinfo=timezone.utc)
	app.logger.propagate = False
	# NOTE: Kept for posterity or future changes.
	# handler_console = logging.StreamHandler(stream=stdout)
	# handler_console.setFormatter(fmt_short)
	# handler_console.setLevel(logging.DEBUG)
	# logger_console = app.logger
	# logger_console.addHandler(handler_console)

	handler_console_error = logging.StreamHandler(stream=stderr)
	handler_console_error.setFormatter(fmt_short)
	handler_console_error.setLevel(log_level)
	logger_console_error = app.logger
	logger_console_error.addHandler(handler_console_error)

	handler_file_app = logging.handlers.TimedRotatingFileHandler(
		log_file_app,
		when='W0',
		backupCount=26,
		encoding='utf-8',
		delay=False,
		utc=True,
		atTime=midnight
	)
	handler_file_app.setFormatter(fmt_long)
	handler_file_app.setLevel(log_level)
	handler_file_app.propagate = False
	logger_file_app = app.logger
	logger_file_app.addHandler(handler_file_app)

	handler_file_db = logging.handlers.TimedRotatingFileHandler(
		log_file_db,
		when='W0',
		backupCount=26,
		encoding='utf-8',
		delay=False,
		utc=True,
		atTime=midnight
	)
	handler_file_db.setFormatter(fmt_long)
	handler_file_db.setLevel(log_level)
	logger_file_db = logging.getLogger('sqlalchemy')
	logger_file_db.propagate = False
	logger_file_db.addHandler(handler_file_db)

	if not secure:
		# Unnessecary in production.
		handler_console_werkzeug = logging.StreamHandler(stream=wsgi_errors_stream)
		handler_console_werkzeug.setFormatter(fmt_short)
		handler_console_werkzeug.setLevel(logging.DEBUG)
		handler_console_werkzeug.propagate = True
		console_werkzeug_logger = logging.getLogger('werkzeug')
		console_werkzeug_logger.addHandler(handler_console_werkzeug)

		handler_file_werkzeug = logging.handlers.TimedRotatingFileHandler(
			log_file_werkzeug,
			when='W0',
			backupCount=26,
			encoding='utf-8',
			delay=False,
			utc=True,
			atTime=midnight
		)
		handler_file_werkzeug.setFormatter(fmt_long)
		handler_file_werkzeug.setLevel(logging.DEBUG)
		logger_file_werkzeug = logging.getLogger('werkzeug')
		logger_file_werkzeug.addHandler(handler_file_werkzeug)

	app.logger.debug('10')
	app.logger.info('20')
	app.logger.warning('30')
	app.logger.error('40')
	app.logger.critical('50')

	app.logger.info(f'Running in {env} mode with log level: {logging.getLevelName(app.logger.level)}')
	app.logger.info('Configured: Logging')
	return None

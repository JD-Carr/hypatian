"""hypatian.config.

Configuration settings for the application.
Many settings are made to 'smart flip' based off:
`FLASK_ENV`, `FLASK_DEBUG`, `FLASK_TESTING`, and `FLASK_SECURE`.
Sensitive settings, or anything you want, should be pulled from
environment variables.
This will make it easier to change keys, secrets, or anything else
without having to rebuild the codebase. Change the environment variable
in the container and just reload apache.
"""
import logging
from os import environ
from pathlib import Path
import sys


def _getbool(variable_name):
	return environ(variable_name).lower() in ['1', 'on', 'true', 't', 'yes']

# App Settings


APP_NAME = 'hypatian'
env = environ['FLASK_ENV']
debug = environ['FLASK_DEBUG'].lower() in ('1', 'on', 't', 'true')
TESTING = environ['FLASK_TESTING'].lower() in ('1', 'on', 't', 'true')
SECURE = environ['FLASK_SECURE'].lower() in ('1', 'on', 't', 'true')

try:
	SECRET_KEY = environ['SECRET_KEY']
except KeyError:
	logging.error('SECRET_KEY does not exist!')
	sys.exit(1)

PROJECT_DIR = Path(__file__).resolve(strict=True).parent.parent
APP_DIR = PROJECT_DIR / 'shuzhai'
APP_LOG_DIR = PROJECT_DIR / 'logs'

# Create log directory, if it doesn't exist.
APP_LOG_DIR.mkdir(exist_ok=True)
if env == 'development':
	DB_DIR = PROJECT_DIR / 'database'
	DB_DIR.mkdir(exist_ok=True)
	db_file = DB_DIR / 'hypatia.sqlite'

# Useful for debugging apache stuff.
APACHE_SERVER_NAME = environ.get('APACHE_SERVER_NAME')
APACHE_RUN_USER = environ.get('APACHE_RUN_USER')
APACHE_RUN_GROUP = environ.get('APACHE_RUN_GROUP')
APACHE_LOG_DIR = environ.get('APACHE_LOG_DIR')
APACHE_RUN_DIR = environ.get('APACHE_RUN_DIR')
APACHE_LOCK_DIR = environ.get('APACHE_LOCK_DIR')
APACHE_VHOSTS_DIR = environ.get('APACHE_VHOSTS_DIR')
APACHE_SSL_SCACHE = environ.get('APACHE_SSL_SCACHE')
APACHE_PID_FILE = environ.get('APACHE_PID_FILE')

"""Flask Settings."""
# Settings specific to the base Flask package should go here.
# All of these variables are built-in to flask.
TESTING: bool = environ['FLASK_TESTING'].lower() in ['1', 'on', 't', 'true']

# Settings that affect the Response jsonify() method.
# Unicodify our jsonify.
JSON_AS_ASCII = False
# Sort JSON's keys alphanumerically for consistent behavior.
JSON_SORT_KEYS = True
# Define the default mimetype for jsonify responses.
JSONIFY_MIMETYPE = 'application/json'
# Responses will be output with newlines, spaces, and indentation for easy reading.
JSONIFY_PRETTYPRINT_REGULAR = debug

# Fild upload, should override in production.
# Limited the maximum allowed payload to 8 megabytes.
# http://flask.pocoo.org/docs/patterns/fileuploads/#improving-uploads
MAX_CONTENT_LENGTH = 8 * 1024 * 1024

# Production should use HTTPS, but fall back to http for development / testing
PREFERRED_URL_SCHEME = 'https://' if SECURE else 'http://'

# Server-side verification timeout for the session cookie.
PERMANENT_SESSION_LIFETIME = 28 * 24 * 60 * 60  # 28 days in seconds (D * H * M * S)

SESSION_COOKIE_NAME = 'session'
SESSION_COOKIE_DOMAIN = False
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SECURE = SECURE

# Improves file speeds with Apache servers.
# This breaks sending files when using development / testing environments
USE_X_SENDFILE = SECURE

"""Flask-Bcrypt."""

if debug or TESTING:
	BCRYPT_LOG_ROUNDS = 4
else:
	BCRYPT_LOG_ROUNDS = 12

"""Flask-Login."""

REMEMBER_COOKIE_NAME = 'rememberme'
REMEMBER_COOKIE_DURATION = 28 * 24 * 60 * 60  # 28 days (D*H*M*S)
REMEMBER_COOKIE_HTTPONLY = True
REMEMBER_COOKIE_SECURE = SECURE
REMEMBER_COOKIE_REFRESH_EACH_REQUEST = False

"""Flask-Login Custom Settings."""

FLASK_LOGIN_MESSAGE = 'Please log in to access page.'
FLASK_LOGIN_MESSAGE_CATEGORY = 'info'
FLASK_LOGIN_SESSION_PROTECTION = 'basic'

# Easily retrieve all the standard session data.
# SESSION_KEYS = {'_user_id', '_remember', '_remember_seconds', '_id', '_fresh', 'next'}
# SESSION_KEYS = set(['_user_id', '_remember', '_remember_seconds', '_id', '_fresh', 'next'])

GOOGLE_CLIENT_ID = environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET_KEY = environ.get("GOOGLE_CLIENT_SECRET_KEY", None)
GOOGLE_DISCOVERY_URL = environ.get('GOOGLE_DISCOVERY_URL', None)


"""Flask-SQLAlchemy Settings."""

SQLALCHEMY_ECHO = False
SQLALCHEMY_RECORD_QUERIES = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

if env == 'development':
	SQLALCHEMY_DATABASE: str = 'SQLite'
	SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_file}'
	SQLALCHEMY_ENGINE_OPTIONS = {
		'pool_pre_ping': True
	}

"""Flask-WTF."""
# Enable protection agains *Cross-site Request Forgery (CSRF)*
# Set Testing to False so we still have authentication when unit testing
WTF_CSRF_ENABLED = not TESTING

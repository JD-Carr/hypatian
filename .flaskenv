# .flaskenv
# vim: ft=sh
#-------------------------------------------------------------------------------#
# Flask Settings
#-------------------------------------------------------------------------------#
# Flask-native settings
# Best exported to environment before running the app.
# This file exists for local development.
# Place these into docker-compose.yml files under `environment:` for test/prod.

# Disables Flask automatically looking for environment files.
# Docker-compose already pre-loads the environment files.
# Not really needed but shaves 0.001ms off that launch time.
FLASK_SKIP_DOTENV=0

# Environment
# Flask recognizes both ‘development’ & ‘production’ as special keywords.
# Using either changes options mostly pertaining to debugging and formatting.
FLASK_ENV=development

# Modifies what gets logged and to what streams.
FLASK_DEBUG=1

# Can also refer directly to a function inside a py file.
# Example: FLASK_APP=hypatian:create_app
FLASK_APP=wsgi.py

FLASK_RUN_HOST=127.0.0.1
FLASK_RUN_PORT=5000

#FLASK_RUN_CERT=
#FLASK_RUN_KEY=

# Flask will detect if any of these files have changed.
# If it detects a file change, it will restart the app.
#FLASK_RUN_EXTRA_FILES=

#-------------------------------------------------------------------------------#
# Flask Custom Settings.
#-------------------------------------------------------------------------------#
# Non-native variables used by this project for configuration settings.
# These are not understood by Flask natively.
FLASK_SECURE=0
FLASK_TESTING=0

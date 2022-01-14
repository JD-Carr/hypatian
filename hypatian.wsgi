#!/var/www/hypatian/.venv/bin/python3
# vim: ft=python
"""Creates mod_wsgi instance of app."""
import os
import sys
from hypatian import create_app

app_dir = os.path.dirname(__file__)

if app_dir not in sys.path:
	sys.path.insert(0, app_dir)

application = create_app()

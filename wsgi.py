# vim: ft=python
"""wsgi.

Entry point for Flask Web Server Gateway Interface (WSGI).
.. note: Should only be used for development and testing
"""
from hypatian import create_app

app = create_app()

if __name__ == '__main__':
	app.run()

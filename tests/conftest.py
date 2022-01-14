"""tests.tests.conftest."""
import pytest

from flask import Flask

from hypatian import create_app
from hypatian.extensions import db as database
from hypatian.models.user import User
# from tests.util import EMAIL, ADMIN_EMAIL, PASSWORD


@pytest.fixture
def app():
	"""Test.

	:return: The app
	:rtype: Flask
	"""
	return create_app()


@pytest.fixture
def client(app):
	with app.test_client() as client:
		yield client

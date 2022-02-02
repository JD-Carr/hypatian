"""hypatian.commands."""
import os

import click
from flask import Flask
from flask import current_app

HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(HERE, os.pardir)
TEST_PATH = os.path.join(PROJECT_ROOT, 'tests')

__all__ = ['register_commands']


def register_commands(app: Flask) -> None:
	"""Register Click commands.

	:param app: app object
	:type app: Flask
	:type: None
	"""
	app.cli.add_command(clean)
	app.cli.add_command(config)
	app.cli.add_command(drop)
	app.cli.add_command(seed)
	app.cli.add_command(printer)
	return None


@current_app.cli.command()
def config() -> None:
	"""Output all Config Variables."""
	click.echo('Custom command - cfg')
	for key in current_app.config:
		val = str(current_app.config[key])
		click.echo('  |- ' + key + ' -> ' + val)
	return None


@current_app.cli.command()
def drop() -> None:
	"""Destroy dev database.

	Create new dev database
	Generate junk data
	"""
	from hypatian.extensions import db
	db.drop_all()
	return None


@current_app.cli.command()
def seed() -> None:
	"""Destroy dev database.

	Create new dev database
	Generate junk data
	"""
	from faker import Faker
	from hypatian.extensions import db
	from hypatian.models import (
		BaseTable,
		InventoryLocation,
		Patient,
		Product,
		ProductCategory,
		UnitOfMeasure
	)
	db.drop_all()
	db.create_all()
	fake = Faker()

	InventoryLocation.create(name='Supply Room')
	InventoryLocation.create(name='North Wing')
	InventoryLocation.create(name='South Wing')
	InventoryLocation.create(name='Car Stock')
	InventoryLocation.create(name='Other')

	ProductCategory.create(name='Miscellaneous')
	ProductCategory.create(name='Barrier/Ointment')
	ProductCategory.create(name='Bowel/Bladder')
	ProductCategory.create(name='Diapers/Pullups/Underpads')
	ProductCategory.create(name='Feeding Tube')
	ProductCategory.create(name='Gloves')
	ProductCategory.create(name='Isolation')
	ProductCategory.create(name='IV Supplies')
	ProductCategory.create(name='Ostomy')
	ProductCategory.create(name='Oxygen')
	ProductCategory.create(name='Socks')
	ProductCategory.create(name='Trach Supplies')
	ProductCategory.create(name='Tubes/Needles/Syringes')
	ProductCategory.create(name='Wound Care')
	ProductCategory.create(name='Urological')

	UnitOfMeasure.create(name='Unknown', abbreviation='UNK', is_base_unit=False)
	UnitOfMeasure.create(name='Bag', abbreviation='BG', is_base_unit=False)
	UnitOfMeasure.create(name='Barrel', abbreviation='BBL', is_base_unit=False)
	UnitOfMeasure.create(name='Bottle', abbreviation='BT', is_base_unit=False)
	UnitOfMeasure.create(name='Box', abbreviation='BX', is_base_unit=False)
	UnitOfMeasure.create(name='Can', abbreviation='CN', is_base_unit=False)
	UnitOfMeasure.create(name='Case', abbreviation='CS', is_base_unit=False)
	UnitOfMeasure.create(name='Carton', abbreviation='CT', is_base_unit=False)
	UnitOfMeasure.create(name='Dozen', abbreviation='DZ', is_base_unit=False)
	UnitOfMeasure.create(name='Each', abbreviation='EA', is_base_unit=True)
	UnitOfMeasure.create(name='Gallon', abbreviation='GAL', is_base_unit=False)
	UnitOfMeasure.create(name='Jar', abbreviation='JR', is_base_unit=False)
	UnitOfMeasure.create(name='Keg', abbreviation='KG', is_base_unit=False)
	UnitOfMeasure.create(name='Kit', abbreviation='KT', is_base_unit=False)
	UnitOfMeasure.create(name='Lot', abbreviation='LT', is_base_unit=False)
	UnitOfMeasure.create(name='Package', abbreviation='PA', is_base_unit=False)
	UnitOfMeasure.create(name='Pair', abbreviation='PR', is_base_unit=True)
	UnitOfMeasure.create(name='Piece', abbreviation='PC', is_base_unit=False)
	UnitOfMeasure.create(name='Set', abbreviation='ST', is_base_unit=False)
	UnitOfMeasure.create(name='Tray', abbreviation='TE', is_base_unit=False)
	UnitOfMeasure.create(name='Tree', abbreviation='TRE', is_base_unit=False)
	UnitOfMeasure.create(name='Tube', abbreviation='TB', is_base_unit=False)
	UnitOfMeasure.create(name='Vial', abbreviation='VL', is_base_unit=False)
	UnitOfMeasure.create(name='Yard', abbreviation='YD', is_base_unit=False)

	Product.create(
		code='ALB90205',
		name='LARGE NON-SKID/SLIP SOCKS 48/CS',
		product_category_id=11,
		issue_unit_of_measure_id=17,
		purchase_unit_of_measure_id=7,
		purchase_unit_to_issue_unit_multiplier=24
	)
	Product.create(
		code='ALB90207',
		name='X-LARGE NON-SKID/SLIP SOCKS 48/CS',
		product_category_id=11,
		issue_unit_of_measure_id=17,
		purchase_unit_of_measure_id=7,
		purchase_unit_to_issue_unit_multiplier=24
	)
	Product.create(
		code='ALB90209',
		name='SMALL NON-SKID/SLIP SOCKS 48/CS',
		product_category_id=11,
		issue_unit_of_measure_id=17,
		purchase_unit_of_measure_id=7,
		purchase_unit_to_issue_unit_multiplier=24
	)
	Product.create(
		code='ALB90210',
		name='MEDIUM NON-SKID/SLIP SOCKS 48/CS',
		product_category_id=11,
		issue_unit_of_measure_id=17,
		purchase_unit_of_measure_id=7,
		purchase_unit_to_issue_unit_multiplier=24
	)
	Product.create(
		code='ALB90211',
		name='2XL NON-SKID/SLIP SOCKS 48/CS',
		product_category_id=11,
		issue_unit_of_measure_id=17,
		purchase_unit_of_measure_id=7,
		purchase_unit_to_issue_unit_multiplier=24
	)
	Product.create(
		code='ALB90219',
		name='3XL NON-SKID/SLIP SOCKS 48/CS',
		product_category_id=11,
		issue_unit_of_measure_id=17,
		purchase_unit_of_measure_id=7,
		purchase_unit_to_issue_unit_multiplier=24
	)

	for _ in range(100):
		Patient.create(
			report=False,
			name_first=fake.first_name(),
			name_last=fake.last_name(),
			date_of_birth=fake.date_object()
		)
	# For patient contacts?
	# import random
	# random.choice(users).id

	for _ in range(10):
		BaseTable.create(
			report=False,
			col_bool=fake.pybool(),
			col_date=fake.date_object(),
			col_datetime=fake.date_time(),
			col_float=fake.pyfloat(left_digits=2, right_digits=2),
			col_varchar=fake.pystr(max_chars=32),
			col_time=fake.time_object()
		)

	return None


@current_app.cli.command()
def get_sa_models() -> None:
	"""Junk."""
	from hypatian.extensions import db
	models = db.Model._decl_class_registry.values()
	model_dict = {}
	for model in models:
		try:
			model_dict[model.__name__] = model
		except AttributeError:
			# Some values may not have ``__name__`` attibute
			pass
	click.echo(model_dict)


@click.command()
def printer() -> None:
	"""Print info.

	.. todo:: Make this print current environment variables.
	"""
	print('HERE: ', HERE)
	print('PROJECT ROOT: ', PROJECT_ROOT)
	print('TEST PATH: ', TEST_PATH)
	return None


@click.command()
def clean() -> None:
	"""Remove *.pyc and *.pyo files recursively starting at current directory.

	Borrowed from Flask-Script, converted to use Click
	"""
	counter: int = 0
	for dirpath, _, filenames in os.walk('.'):
		for filename in filenames:
			if filename.endswith('.pyc') or filename.endswith('.pyo'):
				full_pathname = os.path.join(dirpath, filename)
				click.echo(f'Removing {full_pathname}')
				os.remove(full_pathname)
				counter += 1
	click.echo(f'Removed {counter} file(s)')
	return None


@click.command()
def test():
	"""Run the tests."""
	# import sys
	# import pytest
	# rv = pytest.main([TEST_PATH, '--verbose'])
	# sys.exit(rv)
	click.echo('test')

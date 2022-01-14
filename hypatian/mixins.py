"""hypatian.mixins."""
import datetime
import json
from decimal import Decimal
from pprint import pformat
from typing import (
	Any,
	Dict,
	List,
	Optional,
	Set,
	Union
)

from flask import current_app as app
from sqlalchemy.inspection import inspect
from sqlalchemy.ext.declarative import declared_attr

from hypatian.extensions import db
from hypatian.models.utils import SQLITE_NOW

__all__ = ['CoreMixin']


class CoreMixin:
	"""Provide CRUD operations and data serializations to models.

	Should be loaded into all models
	.. todo:: load this automatically into model paradigm
	"""

	delay_save = False  # if True, prevents saving to table

	@declared_attr
	def created_datetime(cls):
		"""Record date and time record is created."""
		return db.Column(
			db.DateTime(),
			nullable=False,
			server_default=db.text(SQLITE_NOW)
		)

	@declared_attr
	def created_user(cls):
		"""Record user who creates record."""
		return db.Column(
			db.String(128),
			nullable=True,
			server_default='automata'
		)

	@declared_attr
	def updated_datetime(cls):
		"""Record date and time when record is updated."""
		return db.Column(
			db.DateTime(),
			nullable=False,
			server_default=db.text(SQLITE_NOW),
			server_onupdate=db.text(SQLITE_NOW)
		)

	@declared_attr
	def updated_user(cls):
		"""Record user who updates record."""
		return db.Column(
			db.String(128),
			nullable=True,
			server_default='automata',
			server_onupdate='automata'
		)

	def __repr__(self) -> str:
		"""Return debug-friendly string representation of a record.

		:returns: Debug-friendly record identifier
		:rtype: str
		"""
		return f'<{self.__class__.__name__}>'

	def __str__(self) -> str:
		"""Return human-friendly string representation of a record.

		.. note:: Override this in each model class
		:returns: human-friendly record identifier
		:rtype: str
		"""
		return self.__repr__()

	@classmethod
	def __clean_kwargs(cls, kwargs: dict) -> None:
		"""Remove all keyword arguments that are not valid CRUD arguments.

		:param kwargs: Parameters corresponding to column names
		:type kwargs: dict
		:rtype: None
		"""
		cols = cls.__dict__
		remove = [k for k in kwargs if k not in cols and f'_{k}' not in cols and f'{k}_id' not in cols]
		for rem in remove:
			del kwargs[rem]

	@classmethod
	def report(cls, msg: str) -> None:
		"""Record msg to app logger [log level->INFO].

		:param msg: A message to be recorded to the app logger @ INFO level
		:type msg: str
		:rtype: None
		"""
		app.logger.info(msg)

	@classmethod
	def create(cls, commit=True, report=True, **kwargs) -> object:
		"""Create a new record and saves it to the table.

		Calls before_create and after_create just before and after committing the new object
		Override these to change create behavior
		:param commit: Write to database
		:type commit: bool
		:param report: Switches logging on/off
		:type report: bool
		:param kwargs: keyword arguments to be forwarded to class constructor after cleaning
		:type kwargs: dict
		:returns: Created record
		:rtype: object
		"""
		cls.__clean_kwargs(kwargs)
		if report:
			cls.report(f'Creating {cls.__name__}: {pformat(kwargs)}')
		record = cls(**kwargs)
		record.before_create(kwargs)
		db.session.add(record)
		record.save(commit)
		record.after_create(kwargs)
		return record

	def update(self, commit=True, report=True, **kwargs):
		"""Update an object.

		Calls before_update just before updating the object and after_update just after
		committing the object. Override these to change update behavior
		:param commit: write to database
		:type commit: bool
		:param report: log update
		:type report: bool
		:param kwargs: keyword arguments to be updated after cleaning
		:type kwargs: dict
		:returns: updated object
		:rtype:
		"""
		self.__clean_kwargs(kwargs)
		if report:
			self.report(f'Updating {self.__class__.__name__} {self}: {pformat(kwargs)}')
		self.before_update(kwargs)
		for attr, value in kwargs.items():
			setattr(self, attr, value)
		self.save(commit)
		self.after_update(kwargs)
		return self

	def save(self, really=True) -> object:
		"""Commit session if delay_save is False.

		:param really: (boolean): only commit if really is True
		:type really: bool
		:returns: The commited record object.
		:rtype: object
		"""
		if really and not self.delay_save:
			db.session.commit()
		return self

	def delete(self, commit=True, report=True) -> bool:
		"""Delete record.

		Calls after_delete just after deleting the object and just before committing the session.
		Override these to change update behavior.
		:param commit: write to database
		:type commit: bool
		:param report: log deletion
		:type report: bool
		:returns: True is committing, False otherwise
		:rtype: bool
		"""
		if report:
			self.report(f'Deleting {self.__class__.__name__} {self}')
		db.session.delete(self)
		self.after_delete()
		return commit and db.session.commit()

	def before_create(self, values):
		"""Call before record creation."""
		pass

	def after_create(self, values):
		"""Call after record creation."""
		pass

	def before_update(self, values):
		"""Call before record update."""
		pass

	def after_update(self, values):
		"""Call after record update."""
		pass

	def after_delete(self):
		"""Call after record deletion."""
		pass

	@classmethod
	def columns(cls, skip_pk=True, remove='') -> Optional[set[str]]:
		"""Return table's field names.

		includes foreign keys, but not relationships
		:param skip_pk: if set to False, primary keys will be returned
		:type skip_pk: bool
		:param remove: Field names to be skipped, separated by a single space character
		:type remove: str
		:return: Returns set of all field names not in ``remove``.
		:rtype: Optional[set[str]]
		"""
		remove: list = remove.split()
		insp = inspect(cls)
		if skip_pk:
			primary_key = [p.key for p in insp.primary_key]
			remove += primary_key
		cols: set = set(insp.columns.keys()) - set(remove)
		return cols

	@classmethod
	def relationships(cls, remove='') -> Optional[set[str]]:
		"""Return names of the table's relationships.

		:param remove: Relationships to be skipped, separated by a single space character
		:type remove: str
		:returns: Relationships not in ``remove``
		:rtype: Optional[set[str]]
		"""
		remove: list = remove.split()
		cols: set = set(inspect(cls).relationships) - set(remove)
		return cols

	def to_dict(self, remove='') -> dict[str, Any]:
		"""Return all not ignored fields and their data.

		:param remove: record's field's to be ignored, separated by a single space character
		:type remove: str
		:returns: Record's field->data in dictionary format
		:rtype: dict[str, Any]
		"""
		data: dict = {}
		for column in self.columns(remove=remove):  # pylint: disable=no-member
			value = data[column] = getattr(self, column, None)
			if isinstance(value, Decimal):
				data[column] = float(data[column])
			elif isinstance(value, datetime.datetime):
				data[column] = value.isoformat(sep='T', timespec='seconds')
			elif isinstance(value, datetime.date):
				data[column] = value.strftime("%Y-%m-%d")
			elif isinstance(value, datetime.time):
				data[column] = value.strftime("%H:%M:%S")
		return data

	def to_json(self, remove='') -> str:
		"""Return record data in json-formatted serialized form.

		:param remove: record's field's to be ignored, separated by a single space character
		:type remove: str
		:returns: Record data in a JSON-formatted serialized string
		:rtype: str
		"""
		return json.dumps(self.to_dict(remove=remove))

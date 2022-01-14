"""hypatian.utils."""
from datetime import (
	datetime,
	timezone
)


def get_date_format(str_date: str) -> datetime:
	"""
	This function converts string into date type object
	:param str_date: Date in string format
	:type str_date: str
	:returns: object of given time
	:rtype: datetime
	:TODO: Add tzaware.
	"""
	str_date = str_date.split("T")[0]
	return datetime.strptime(str_date, "%Y-%m-%d")


def now() -> str:
	"""
	Get a ISO-8601 datetime format using UTC and offset
	Length should be a static 29 characters
	Includes offset as +00:00 format, no letters
	:returns: ISO-8601 formatted date
	:rtype: str
	"""
	return datetime.utcnow().replace(tzinfo=timezone.utc).isoformat(sep='T', timespec='seconds')

"""Utility functions for models."""

# Note: python datetime can't parse the date if it has a `T` separator.
SQLITE_NOW = "(strftime('%Y-%m-%d %H:%M:%f+00:00', 'now'))"
# SQLITE_NOW = "(strftime('%Y-%m-%dT%H:%M:%f+00:00', 'now'))"

# SQLITE_AGE = 'DATEDIFF(DAY, @date_of_birth, GetDate()) / 365.25'
# SELECT TIMESTAMPDIFF( YEAR, date_of_birth,  CURDATE()) AS age;

# Add code to check database and change schemas.
# Probably need mixin's for different schemas.

__all__ = [
	'SQLITE_NOW'
]

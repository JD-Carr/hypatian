"""tests.test_eg."""


def func(num: int) -> int:
	"""Add one to an integer.

	:param num: An integer
	:type num: int
	:return: passed integer + 1
	:rtype: int
	"""
	return num + 1


def test_answer():
	"""Test `func`

	:return: The result
	"""
	assert func(4) == 5

"""tests.test_main."""


def test_health(client):
	"""Test main health.

	:return: Test
	"""
	response = client.get('/health')
	assert response.status_code == 200

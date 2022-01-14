"""hypatian.api.utils."""
# from flask import (
# 	Response,
# 	jsonify,
# 	make_response,
# 	request
# )
#
#
# class ResponseMixin(Response):
# 	"""Overide and add some common attributes for api responeses."""
#
# 	def __init__(self, response, **kwargs):
# 		"""Define response initialization."""
# 		if 'mimetype' not in kwargs and 'contenttype' not in kwargs:
# 			if response.startswith('<?json'):
# 				kwargs['mimetype'] = 'application/json'
# 		return super(ResponseMixin, self).__init__(response, **kwargs)
#
# 	@classmethod
# 	def force_type(cls, rv, environ=None):
# 		"""Force typing."""
# 		if isinstance(rv, str):
# 			return super(ResponseMixin, cls).force_type({"message": rv}, environ)
#
# 		if isinstance(rv, dict):
# 			rv = jsonify(rv)
# 		return super(ResponseMixin, cls).force_type(rv, environ)

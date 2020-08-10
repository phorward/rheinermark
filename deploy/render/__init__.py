from server import request
from server.render import admin, html, json, vi, xml

@html.utils.jinjaGlobalFilter
def isList(render, val):
	return isinstance(val, list)

@html.utils.jinjaGlobalFilter
def isDict(render, val):
	return isinstance(val, dict)

@html.utils.jinjaGlobalFunction
def setMimeType(render, mimetype):
	request.current.get().response.headers["Content-Type"] = mimetype

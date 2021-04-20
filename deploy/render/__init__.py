# -*- coding: utf-8 -*-
from server import request, conf
from server.render import admin, html, json, vi, xml
import logging


@html.utils.jinjaGlobalFilter
def isList(render, val):
	return isinstance(val, list)

@html.utils.jinjaGlobalFilter
def isDict(render, val):
	return isinstance(val, dict)

@html.utils.jinjaGlobalFunction
def setMimeType(render, mimetype):
	request.current.get().response.headers["Content-Type"] = mimetype

@html.utils.jinjaGlobalFunction
def betterExecRequest(render, path, *args, **kwargs):
	"""
	░░░░░░░░░░░█▀▀░░█░░░░░░
	░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░
	░░░░░░█░█░░░░░░░░░░▐░░░
	░░░░░░▐▐░░░░░░░░░▄░▐░░░
	░░░░░░█░░░░░░░░▄▀▀░▐░░░
	░░░░▄▀░░░░░░░░▐░▄▄▀░░░░
	░░▄▀░░░▐░░░░░█▄▀░▐░░░░░
	░░█░░░▐░░░░░░░░▄░█░░░░░
	░░░█▄░░▀▄░░░░▄▀▐░█░░░░░
	░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░
	░░▐█▐▄░░█░░░░░░▐░█▄▄░░
	░░░▀▀░▄ViUR▄░░░▐▄▄▄▀░░░
	"""
	currentRequest = request.current.get()
	tmp_params = currentRequest.kwargs.copy()
	currentRequest.kwargs = {"__args": args, "__outer": tmp_params}
	currentRequest.kwargs.update( kwargs )
	lastRequestState = currentRequest.internalRequest
	currentRequest.internalRequest = True
	caller = conf["viur.mainApp"]
	pathlist = path.split("/")

	for currpath in pathlist:
		if currpath in dir( caller ):
			caller = getattr( caller,currpath )
		elif "index" in dir( caller ) and  hasattr( getattr( caller, "index" ), '__call__'):
			caller = getattr( caller, "index" )
		else:
			currentRequest.kwargs = tmp_params # Reset RequestParams
			currentRequest.internalRequest = lastRequestState
			return( u"Path not found %s (failed Part was %s)" % ( path, currpath ) )

	if (not hasattr(caller, '__call__')
		or ((not "exposed" in dir( caller )
			    or not caller.exposed))
		and (not "internalExposed" in dir( caller )
				or not caller.internalExposed)):
		currentRequest.kwargs = tmp_params # Reset RequestParams
		currentRequest.internalRequest = lastRequestState
		return( u"%s not callable or not exposed" % str(caller) )

	try:
		# ...
		if "style" in kwargs:
			kwargs = kwargs.copy()
			del kwargs["style"]

		resstr = caller( *args, **kwargs )
	except Exception as e:
		logging.error("Caught execption in execRequest while calling %s" % path)
		logging.exception(e)
		raise

	currentRequest.kwargs = tmp_params
	currentRequest.internalRequest = lastRequestState

	return resstr

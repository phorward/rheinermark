#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#                 iii
#                iii
#               iii
#
#           vvv iii uu      uu rrrrrrrr
#          vvvv iii uu      uu rr     rr
#   v     vvvv  iii uu      uu rr     rr
#  vvv   vvvv   iii uu      uu rr rrrrr
# vvvvv vvvv    iii uu      uu rr rrr
#  vvvvvvvv     iii uu      uu rr  rrr
#   vvvvvv      iii  uu    uu  rr   rrr
#    vvvv       iii   uuuuuu   rr    rrr
#
#   I N F O R M A T I O N    S Y S T E M
# ------------------------------------------------------------------------------
#
# Project:      rheinermark-viur
# Initiated:    2019-11-14 17:16:31
# Copyright:    Jan Max Meyer, Phorward Software Technologies
# Author:       Max
#
# ------------------------------------------------------------------------------

from server import conf, securityheaders, request
from collections import OrderedDict

# ------------------------------------------------------------------------------
# General configuration
#

#conf["viur.disableCache"] = True
#conf["viur.debug.traceExternalCallRouting"] = True

# Set cookie lifeTime to 4 months
conf["viur.session.lifeTime"] = 4*24*60*60

# ------------------------------------------------------------------------------
# Project-specific configuration
#

conf["project.user.interests"] = {
	"microlight": u"Ultraleichtflug",
	"soaring": u"Segelflug",
	"motorglider": u"Motorsegelflug",
	"newsletter": u"Newsletter (WICHTIG!)",
	"trainee": u"Flugschüler",
	"youth": u"Jugendgruppe",
	"website": u"Webseite - Information über Aktualisierungen erhalten",
	"beta": u"Webseite - Neue Funktionen ausprobieren (Betatest)"
}

conf["project.appointment.duties"] = OrderedDict([
	("trainer", u"Fluglehrer"),
	("controller", u"Flugleiter"),
	("canteen", u"Kantine"),
	#("towlaunch", u"Schlepppilot"),
	("winch", u"Windenfahrer")
])

# ------------------------------------------------------------------------------
# ViUR admin tool specific configurations
#

conf["admin.vi.name"] = "LSV Ruhr-Lenne Iserlohn e.V."

#conf["admin.moduleGroups"] = [
#	{"prefix":u"Start: ", "name": u"Starterfassung", "icon": "icons/modules/tickets.svg"},
#]

# ---------------------------------------------------------------------------------------------------------------------
# Request preprocessor
#

def handleRequest(path):
	"""
	This simple request preprocessor can be used to canalize all requests coming
	from several domains and 301 redirects them to a main URL.
	"""
	if "X-AppEngine-TaskName" in request.current.get().request.headers:
		return path

	mainUrl = "https://www.segelfliegen.com"
	url = request.current.get().request.url.lower()

	if not url.startswith(mainUrl):
		for proto in ["http://", "https://"]:
			if url.startswith(proto):
				for other in ["segelfliegen.com"]:
					#logging.debug("url = %r startswith = %r", url[len(proto):], other)

					if url[len(proto):].startswith(other):
						raise server.errors.Redirect(mainUrl + url[len(proto) + len(other):], status=301)

	return path

conf["viur.requestPreprocessor"] = handleRequest

# ------------------------------------------------------------------------------
# Error Handler

def errorHandler(e) :
	from server import errors
	from server.render.html import default as Render
	import traceback
	from StringIO import StringIO

	render = Render()

	if isinstance(e, errors.HTTPException) :
		code = int(e.status)
		name = e.name
		descr = e.descr
	else:
		code = 500
		name = "Internal Server Error"
		descr = "An internal server error occured"

	strIO = StringIO()
	traceback.print_exc(file=strIO)
	tbstr = strIO.getvalue().replace( "\n", "--br--" ).replace( " ", "&nbsp;" ).replace( "--br--", "<br />" )

	return render.view({
		"name": name,
		"code": code,
		"descr": descr,
		"traceback" : tbstr
	}, tpl="error")


conf["viur.errorHandler"] = errorHandler

# ------------------------------------------------------------------------------
# Content Security Policy

conf["viur.security.contentSecurityPolicy"] = {}  # Disable this piece of junk.
conf["viur.security.xFrameOptions"] = None

#securityheaders.addCspRule("script-src", "unsafe-inline", "enforce")
#securityheaders.addCspRule("script-src", "unsafe-eval", "enforce")
#securityheaders.addCspRule("script-src", "www.google.com", "enforce")
#securityheaders.addCspRule("script-src", "www.gstatic.com", "enforce")
#securityheaders.addCspRule("font-src", "fonts.gstatic.com", "enforce")

# ------------------------------------------------------------------------------
# Server startup
#

import server, modules, render

server.setDefaultLanguage("de") #set default language!
application = server.setup(modules, render)

if __name__ == "__main__":
	server.run()

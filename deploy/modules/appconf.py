# -*- coding: utf-8 -*-
from server.prototypes.singleton import Singleton

class appconf(Singleton):

	adminInfo = {
		"name": u"Einstellungen",
		"handler": "singleton",
	    "icon": "icons/modules/settings.svg"
	}

	def canView(self):
		return True

appconf.html = True

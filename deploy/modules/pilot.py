# -*- coding: utf-8 -*-
from server.prototypes.list import List
from server import request


class Pilot(List):

	adminInfo = {
		"name": u"Start: Pilot",
	    "handler": "list.member",
	    "icon": "icons/modules/users.svg",
		"columns": ["firstname", "lastname"]
	}

	def listFilter(self, query):
		if request.current.get().kwargs.get("secret") == "bea6846f04709ed":
			return query

		return super(Pilot, self).listFilter(query)


Pilot.json = True

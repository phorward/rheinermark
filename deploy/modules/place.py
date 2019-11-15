# -*- coding: utf-8 -*-
from server.prototypes.list import List
from server import request

class Place(List):

	adminInfo = {
		"name": u"Start: Flugplatz",
		"handler": "list.place",
		"icon": "icons/modules/locations.svg",
		"filter":{"orderby":"name"},
		"columns": ["name","icao"]
	}

	def listFilter(self, query):
		if request.current.get().kwargs.get("secret") == "bea6846f04709ed":
			return query

		return super(Place, self).listFilter(query)


Place.json = True

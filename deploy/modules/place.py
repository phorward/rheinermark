# -*- coding: utf-8 -*-
from server.prototypes.list import List
from server import request


class Place(List):

	adminInfo = {
		"name": u"Flugplatz",
		"handler": "list.place",
		"icon": "icons/modules/locations.svg",
		"filter":{"orderby":"name"},
		"columns": ["name","icao"]
	}

	adminInfo = None  # tmp

	roles = {
		"*": ["view"],
		"executive": ["view", "add", "edit", "delete"]
	}

Place.json = True

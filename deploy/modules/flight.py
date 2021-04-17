# -*- coding: utf-8 -*-
from server.prototypes.list import List

class Flight(List):

	adminInfo = {
		"name": u"Flugdaten",
		"handler": "list.flight",
		"icon": "icons/modules/tickets.svg",
		"columns": ["name", "icao"],
	}

	adminInfo = None  # tmp

	roles = {
		"*": ["view", "add"]
	}

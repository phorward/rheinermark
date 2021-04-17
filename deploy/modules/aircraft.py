# -*- coding: utf-8 -*-
from prototypes import SortedList
from skeletons.equipment import equipmentSkel
from server import request
from server.render.html import default as htmlRender

class Aircraft(SortedList):
	listTemplate = "aircraft_list"
	viewTemplate = "aircraft_view"

	adminInfo = {
		"name": u"Flugzeug",
		"columns": ["sortindex", "aircraftkind", "reg", "name", "seats"],
		"handler": "list.aircraft",
		"icon": "icons/modules/list.svg",
	}
	adminInfo = None #tmp

	roles = {
		"*": ["view"],
		"executive": ["view", "add", "edit", "delete"]
	}

	def listFilter(self, query):
		query = super(Aircraft, self).listFilter(query)
		if not query:
			return None

		query.filter("kind", "aircraft")

		if isinstance(self.render, htmlRender):
			query.filter("is_clubowned", True)
			return query

		return query

	def editSkel(self):
		skel = equipmentSkel.subSkel("aircraft").ensureIsCloned()
		skel.kind.readOnly = True
		skel.kind.visible = False
		return skel

	def viewSkel(self):
		return self.editSkel()

	def addSkel(self):
		skel = self.editSkel()
		skel["kind"] = "aircraft"
		return skel

Aircraft.json = True

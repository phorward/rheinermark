# -*- coding: utf-8 -*-
from prototypes import SortedList
from skeletons.equipment import equipmentSkel
from server.render.html import default as htmlRender
from server import utils, exposed

class Aircraft(SortedList):
	listTemplate = "aircraft_list"
	viewTemplate = "aircraft_view"

	adminInfo = {
		"name": u"Flugzeug",
		"columns": ["sortindex", "aircraftkind", "reg", "name", "seats"],
		"handler": "list.aircraft",
		"icon": "icons/modules/list.svg",
	}

	roles = {
		"*": ["view"],
		"executive": ["view", "add", "edit", "delete"]
	}

	def listFilter(self, query):
		query.filter("kind", "aircraft")

		if not query.getOrders():
			query.order("sortindex")

		# All club aircraft are exposed, as they are not considered to be "private"
		if isinstance(self.render, htmlRender) or not utils.getCurrentUser():
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

	@exposed
	def index(self, *args, **kwargs):
		return self.list(*args, **kwargs)


Aircraft.json = True

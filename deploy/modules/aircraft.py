# -*- coding: utf-8 -*-
from server.prototypes.list import List
from skeletons.equipment import equipmentSkel
from server import request

class Aircraft(List):

	adminInfo = {
		"name": u"Start: Flugzeug",
		"columns": ["aircraftkind", "reg", "name", "seats"],
		"handler": "list.aircraft",
		"icon": "icons/modules/list.svg",
	}

	def listFilter(self, query):
		query.filter("kind", "aircraft")

		if request.current.get().kwargs.get("secret") == "bea6846f04709ed":
			return query

		return super(Aircraft, self).listFilter(query)

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

# -*- coding: utf-8 -*-
from server.prototypes.list import List
from skeletons.equipment import equipmentSkel


class Winch(List):

	adminInfo = {
		"name": u"Start: Winde",
		"columns": ["reg", "name"],
		"handler": "list.aircraft",
		"icon": "icons/modules/list.svg",
	}

	def editSkel(self):
		skel = equipmentSkel.subSkel("winch").ensureIsCloned()
		skel.kind.readOnly = True
		skel.kind.visible = False
		return skel

	def viewSkel(self):
		return self.editSkel()

	def addSkel(self):
		skel = self.editSkel()
		skel["kind"] = "winch"
		return skel

	def listFilter(self, filter):
		filter.filter("kind", "winch")
		return filter

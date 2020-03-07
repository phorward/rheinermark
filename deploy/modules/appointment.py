# -*- coding: utf-8 -*-
from server.prototypes.list import List
from server import request, conf, utils
from server.render.html import default as htmlRender
import logging


class Appointment(List):
	viewTemplate = "appointment_view"

	adminInfo = {
		"name": u"Termin",
		"handler": "list.appointment",
		"icon": "icons/modules/calendar.svg",
		"filter": {"orderby": "date", "orderdir": 1},
		"context": {"kind": "meeting"},
		"columns": ["date", "name"],
		"preview": "/{{module}}/view/{{key}}",
		#"disabledFunctions": ["add", "edit"],
	}

	roles = {
		"*": ["view"],
		"executive": ["view", "add", "edit", "delete"]
	}

	def listFilter(self, query):
		query = super(Appointment, self).listFilter(query)
		if not query:
			return None

		query.filter("kind", "meeting")

		cuser = utils.getCurrentUser()

		if cuser and isinstance(self.render, htmlRender):
			user = conf["viur.mainApp"].user.viewSkel()

			if user.fromDB(cuser["key"]):
				query.filter("recipients IN", user["interests"])

		return query

	def addSkel(self):
		skel = super(Appointment, self).addSkel().subSkel("meeting")
		skel["kind"] = "meeting"

		return skel

	viewSkel = editSkel = addSkel


class Duty(List):
	kindName = "appointment"
	viewTemplate = "duty_view"
	_columns = ["date", "user"]

	adminInfo = {
		"name": u"Dienstplan",
		"handler": "list.duty",
		"icon": "icons/modules/event-planner.svg",
		"filter": {"orderby": "date", "orderdir": 1},
		"context": {"kind": "duty"},
		"columns": ["duty"] + _columns,
		"preview": "/{{module}}/view/{{key}}",
		#"disabledFunctions": ["add", "edit"],
		"views": [
			{
				"name": name,
				"+context": {
					"duty": key
				},
				"columns": _columns
			} for key, name in conf["project.appointment.duties"].items()
		]
	}

	def addSkel(self):
		skel = super(Duty, self).addSkel().subSkel("duty").ensureIsCloned()

		skel["kind"] = "duty"
		skel.name.readOnly = True
		skel.name.required = False
		skel.name.visible = False

		duty = request.current.get().kwargs.get("duty")
		if duty:
			skel.duty.readOnly = True
			skel.duty.visible = False
			skel.duty.required = False
			skel.setBoneValue("duty", duty)

		return skel

	viewSkel = editSkel = addSkel

	def listFilter(self, query):
		query = super(Duty, self).listFilter(query)
		if not query:
			return None

		query.filter("kind", "duty")

		cuser = utils.getCurrentUser()
		if cuser and isinstance(self.render, htmlRender):
			query.mergeExternalFilter({"user.dest.key": cuser["key"]})

		print(query.getFilter())

		return query


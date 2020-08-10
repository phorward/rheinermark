# -*- coding: utf-8 -*-
from server.skeleton import Skeleton
from server.bones import *
from bones import *

from server import conf


class appointmentSkel(Skeleton):
	subSkels = {
		"*": ["kind", "date", "name"],
		"meeting": ["until", "allday", "attachments", "recipients"],
		"duty": ["duty", "user"]
	}

	kind = selectBone(
		descr=u"Art",
		indexed=True,
		visible=False,
		readOnly=True,
		values={
			"duty": u"Dienst",
			"meeting": u"Versammlung"
		}
	)

	duty = selectBone(
		descr=u"Dienst",
		indexed=True,
		required=True,
		values=conf["project.appointment.duties"]
	)

	date = dateBone(
		descr=u"Termin um",
		required=True,
		indexed=True
	)

	allday = booleanBone(
		descr=u"Ganztägig",
		indexed=True,
		defaultValue=True,
		params={
			"tooltip": "Wenn nicht gesetzt wird die Uhrzeit mit ausgegeben!"
		}
	)

	until = dateBone(
		descr=u"Termin bis"
	)

	name = stringBone(
		descr=u"Titel",
		required=True,
		searchable=True,
		indexed=True
	)

	attachments = fileBone(
		descr=u"Anhang",
		multiple=True
	)

	user = userBone(
		descr=u"Benutzer",
		parentKeys=["key", "kind"],
		indexed=True,
		multiple=True,
		required=True
	)

	recipients = selectBone(
		descr=u"Zielgruppe",
		indexed=True,
		required=True,
		multiple=True,
		defaultValue=["newsletter"],
		sortBy="values",
		values=conf["project.user.interests"],
		params={
			"tooltip": u"Auswahl von Zielgruppen."
		}
	)

	def toDB(self, *args, **kwargs):
		if "until" in self and self["until"] and self["until"] < self["date"]:
			self["until"] = None

		return super(appointmentSkel, self).toDB(*args, **kwargs)

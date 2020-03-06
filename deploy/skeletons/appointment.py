# -*- coding: utf-8 -*-
from server.skeleton import Skeleton
from server.bones import *
from bones import *

from server import conf


class appointment(Skeleton):
	subSkels = {
		"*": ["kind", "date", "name"],
		"meeting": ["descr", "attachments", "recipients"],
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
		descr=u"Termin",
		required=True,
		indexed=True
	)

	name = stringBone(
		descr=u"Titel",
		required=True,
		searchable=True,
		indexed=True
	)

	descr = textBone(
		descr=u"Beschreibung",
		searchable=True
	)

	attachments = fileBone(
		descr=u"Anhang",
		multiple=True
	)

	user = userBone(
		descr=u"Benutzer",
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

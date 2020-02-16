# -*- coding: utf-8 -*-
from server.skeleton import Skeleton
from server.bones import *
from server import conf


class newsletter(Skeleton):

	sent = booleanBone(
		descr=u"Verschickt",
		defaultValue=False,
		indexed=True,
		readOnly=True
	)

	sentdate = dateBone(
		descr=u"Verschickt am",
		indexed=True,
		readOnly=True
	)

	name = stringBone(
		descr=u"Titel",
		required=True,
		searchable=True,
		indexed=True
	)

	content = textBone(
		descr=u"Inhalt",
		required=True,
		searchable=True,
		params={
			"tooltip": u"Bitte keine Ansprache verwenden, diese wird automatisch generiert!"
		}
	)

	recipients = selectBone(
		descr=u"Zielgruppe",
		required=True,
		multiple=True,
		defaultValue=["newsletter"],
		sortBy="values",
		values=conf["project.user.interests"],
		params={
			"tooltip": u"Auswahl von Zielgruppen. Bitte diese mit Bedacht wählen!"
		}
	)

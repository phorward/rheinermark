# -*- coding: utf-8 -*-
from server.bones import *
from bones import *
from server.skeleton import Skeleton
from collections import OrderedDict

class messageSkel(Skeleton):
	key = None

	user = userBone(
		descr=u"Absender",
		readOnly=True,
		visible=False
	)

	division = selectBone(
		descr=u"Empfänger",
		values=OrderedDict([
			("executive", "Vorstand"),
			("training_glider", "Ausbildung - Segelflug"),
			("training_microlight", "Ausbildung - Ultraleicht"),
			("website", "Website und Mitgliedersystem")
		]),
		defaultValue="website",
		required=True
	)

	message = textBone(
		descr=u"Deine Mitteilung",
		required=True,
		validHtml=None
	)

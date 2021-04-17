#-*- coding: utf-8 -*-
from server.skeleton import Skeleton
from server.bones import *


class newsSkel(Skeleton):

	online = booleanBone(
		descr=u"Aktiv",
		defaultValue=False,
		indexed=True
	)

	date = dateBone(
		descr=u"Datum",
		indexed=True,
		time=False,
		required=True
	)

	title = stringBone(
		descr=u"Überschrift",
		required=True
	)

	images = fileBone(
		descr=u"Bilder",
		multiple=True
	)

	content = textBone(
		descr=u"Inhalt",
		required=True
	)

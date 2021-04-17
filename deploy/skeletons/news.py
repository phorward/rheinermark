#-*- coding: utf-8 -*-
from server.skeleton import Skeleton
from server.bones import *
import datetime


class newsSkel(Skeleton):

	online = booleanBone(
		descr=u"Aktiv",
		defaultValue=True,
		indexed=True
	)

	date = dateBone(
		descr=u"Datum",
		indexed=True,
		defaultValue=datetime.datetime.now,
		time=False,
		required=True
	)

	title = stringBone(
		descr=u"Überschrift",
		required=True
	)

	teaser = fileBone(
		descr=u"Teaserbild",
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

# -*- coding: utf-8 -*-
from server.skeleton import Skeleton
from server.bones import *


class pilotSkel(Skeleton):
	firstname = stringBone(
		descr=u"Vorname",
		required=True,
		indexed=True,
		searchable=True
	)

	lastname = stringBone(
		descr=u"Nachname",
		required=True,
		indexed=True,
		searchable=True
	)

	nickname = stringBone(
		descr=u"Spitzname",
		indexed=True,
		searchable=True
	)

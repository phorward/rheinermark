# -*- coding: utf-8 -*-
from server.skeleton import Skeleton
from server.bones import *


class place(Skeleton):

	name = stringBone(
		descr=u"Bezeichnung",
		required=True,
		searchable=True,
		indexed=True
	)

	standard = booleanBone(
		descr=u"Standardauswahl",
		indexed=True
	)

	shortname = stringBone(
		descr=u"Kurzname",
		searchable=True,
		indexed=True
	)

	icao = stringBone(
		descr=u"ICAO-Kürzel",
		searchable=True,
		indexed=True
	)

	frequenz = stringBone(
		descr=u"Frequenz"
	)
	photo = fileBone(
		descr=u"Foto"
	)
	voc = fileBone(
		descr=u"Anflugkarte"
	)

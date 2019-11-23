# -*- coding: utf-8 -*-
from server.bones import *
from server.skeleton import Skeleton
import sys, time

class equipmentSkel(Skeleton):

	subSkels = {
		"*": [
			"sortindex",
			"kind",
			"reg",
			"name",
			"photo",
			"is_launcher",
			"is_clubowned",
			"description",
			"documents",
			"wikipedia"
		],
		"aircraft": [
			"photo3side",
			"compreg",
			"aircraftkind",
			"seats",
			"is_selfstarter"
		],
		"winch": [
		]
	}

	sortindex = numericBone(
		descr="SortIndex",
		indexed=True,
		visible=False,
		readOnly=True,
		mode="float",
		max=sys.maxint
	)

	kind = selectBone(
		descr=u"Art",
		values={
			"aircraft": u"Flugzeug",
			"winch": u"Winde"
		},
		defaultValue="plane",
		required=True,
		indexed=True
	)

	reg = stringBone(
		descr=u"Kennzeichen",
		required=True,
		indexed=True,
		searchable=True,
		unique=u"Dieses Kennzeichen wurde bereits einem anderem Objekt zugeordnet!"
	)

	compreg = stringBone(
		descr=u"Wettbewerbskennzeichen",
		indexed=True,
		searchable=True,
		unique=u"Dieses Kennzeichen wurde bereits einem anderem Objekt zugeordnet!"
	)

	name = stringBone(
		descr=u"Bezeichnung",
		required=True,
		searchable=True
	)

	aircraftkind = selectBone(
		descr=u"Flugzeug-Art",
		values={
			"glider": u"Segelflugzeug",
			"microlight": u"Ultraleichtflugzeug",
			"motorglider": u"Motorsegler",
			"aircraft": u"Motorflugzeug"
		},
		indexed=True,
		required=True
	)

	photo = fileBone(
		descr=u"Foto"
	)

	photo3side = fileBone(
		descr=u"3-Seiten-Ansicht"
	)

	seats = numericBone(
		descr=u"Anzahl Sitze",
		precision=0,
		defaultValue=1,
		required=True
	)

	is_selfstarter = booleanBone(
		descr=u"Ist Eigenstartfähig",
		indexed=True,
		defaultValue=False
	)

	is_launcher = booleanBone(
		descr=u"Ist Schleppgerät für Segelflugzeuge",
		indexed=True,
		defaultValue=False
	)

	is_clubowned = booleanBone(
		descr=u"Vereinseigentum",
		indexed=True,
		defaultValue=False
	)

	description = textBone(
		descr=u"Bescheibung, Technische Daten"
	)

	wikipedia = stringBone(
		descr=u"Wikipedia Link"
	)

	documents = fileBone(
		descr=u"Dokumente",
		multiple=True
	)

	def toDB(self, *args, **kwargs):
		if not self["sortindex"]:
			self["sortindex"] = time.time()

		return super(equipmentSkel, self).toDB(*args, **kwargs)

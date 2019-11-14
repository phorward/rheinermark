# -*- coding: utf-8 -*-
from server.bones import *
from server.skeleton import Skeleton


class equipmentSkel(Skeleton):

	subSkels = {
		"*": [
			"kind",
			"reg",
			"name",
			"photo",
			"is_launcher"
		],
		"aircraft": [
			"compreg",
			"aircraftkind",
			"seats",
			"is_selfstarter",
		],
		"winch": [
		]
	}

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
			"aircraft": u"Motorflugzeug"},
	    indexed=True,
	    required=True
	)

	photo = fileBone(
		descr=u"Foto"
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


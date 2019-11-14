# -*- coding: utf-8 -*-
from server.bones import *
from server.skeleton import Skeleton

class flightSkel(Skeleton):
	kindName = "flight"
	searchIndex = "flight"

	aircraft = relationalBone(
		kind="equipment",
		module="aircraft",
		descr="Luftfahrzeug",
		indexed=True,
		required=True,
	    refKeys=["key", "name", "reg", "aircraftkind", "is_selfstarter", "is_launcher"],
		format="$(dest.reg) $(dest.name)"
	)

	launcher = relationalBone(
		kind="equipment",
		module="launcher",
		descr="Starter",
		indexed=True,
		refKeys=["key", "name", "reg"],
		format="$(reg) $(name)"
	)

	pilot = relationalBone(
		kind="pilot",
		descr="Pilot",
		required=True,
		indexed=True,
	    refKeys=["key", "name", "firstname", "lastname"],
		format="$(dest.lastname), $(dest.firstname)"
	)

	passenger = relationalBone(
		kind="pilot",
		descr="Begleiter",
		indexed=True,
		refKeys=["key", "name", "firstname", "lastname"],
		format="$(dest.lastname), $(dest.firstname)"
	)

	takeoff_time = dateBone(
		descr=u"Startzeit",
		required=True,
		indexed=True,
		time=True
	)
	takeoff_at = relationalBone(
		kind="place",
	    descr=u"Start in",
		required=True,
		indexed=True
	)

	touchdown_time = dateBone(
		descr=u"Landezeit",
		required=True,
		indexed=True
	)
	touchdown_at = relationalBone(
		kind="place",
	    descr=u"Landung in",
		required=True,
		indexed=True
	)

	comment = stringBone(
		descr=u"Bemerkung"
	)

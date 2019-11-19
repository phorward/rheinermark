# -*- coding: utf-8 -*-
from server import skeleton
from server.bones import *
from server.modules.user import userSkel as userSkelBase

class userSkel(skeleton.Skeleton):
	subSkels = {
		"public": ["image", "firstname", "lastname", "responsibility"]
	}

	name = emailBone(descr="E-Mail", caseSensitive=False, searchable=True, indexed=True, unique=True)
	password = passwordBone(descr="Password", required=False, readOnly=True, visible=False)

	uid = stringBone(descr="Google's UserID", indexed=True, required=True, readOnly=True, unique=True, visible=False)
	gaeadmin = booleanBone(descr="Is GAE Admin", defaultValue=False, readOnly=True, visible=False)

	access = selectAccessBone(descr="Access rights", values={"root": "Superuser"}, indexed=True)
	status = selectBone(descr="Account status",
	                    values={1: "Waiting for email verification",
	                            2: "Waiting for verification through admin",
	                            5: "Account disabled",
	                            10: "Active"},
	                    defaultValue="10", required=True, indexed=True)
	lastlogin = dateBone(descr="Last Login", readOnly=True, indexed=True)

	image = fileBone(
		descr=u"Foto"
	)

	viewname = stringBone(
		descr=u"Anzeigename",
		readOnly=True,
		indexed=True
	)

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

	responsibility = stringBone(
		descr=u"Aufgabenbereich",
		searchable=True
	)

	visible = booleanBone(
		descr=u"Sichtbar",
		indexed=True,
		defaultValue=False
	)

	sortindex = numericBone(
		descr=u"Sortierungspunktzahl",
		indexed=True,
		defaultValue=1
	)

# -*- coding: utf-8 -*-
from server import skeleton, conf
from server.bones import *
from bones import *
from server.modules.user import userSkel as userSkelBase

from collections import OrderedDict


class userSkel(skeleton.Skeleton):
	subSkels = {
		"restricted": ["firstname", "lastname", "nickname"]
	}

	roles = {
		"executive": ["view", "add", "edit", "delete"]
	}

	uid = stringBone(descr="Google's UserID", indexed=True, readOnly=True, unique=True, visible=False)
	gaeadmin = booleanBone(descr="Is GAE Admin", defaultValue=False, readOnly=True, visible=False)

	status = selectBone(
		descr="Account status",
		values={1: "Waiting for email verification",
				2: "Waiting for verification through admin",
				5: "Account disabled",
				10: "Active"},
		defaultValue="10", required=True, indexed=True
	)

	lastlogin = dateBone(
		descr="Last Login",
		readOnly=True,
		indexed=True
	)

	viewname = stringBone(
		descr=u"Anzeigename",
		readOnly=True,
		indexed=True
	)

	name = emailBone(
		descr="E-Mail",
		caseSensitive=False,
		searchable=True,
		indexed=True,
		unique=True,
		required=True,
	)

	password = passwordBone(
		descr="Password",
		readOnly=True,
		visible=False,
	)

	changepassword = booleanBone(
		descr=u"Passwortänderung erzwingen"
	)

	airbatch_daec = stringBone(
		descr=u"DAeC-Mitglieds-Nr.",
		searchable=True
	)

	airbatch = booleanBone(
		indexed=True,
		readOnly=True,
		visible=False
	)

	firstname = stringBone(
		descr=u"Vorname",
		required=True,
		indexed=True,
		searchable=True,
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

	# Access
	role = selectBone(
		descr=u"Rolle",
		required=True,
		indexed=True,
		defaultValue="user",
		values=OrderedDict([
			("member", u"Mitglied"),
			("executive", u"Vorstand"),
			("user", u"Benutzerdefiniert / Manuell")
		]),
		params={"category": u"Zugriffsrechte"}
	)

	# Interests
	interests = selectBone(
		descr=u"Interessen",
		required=True,
		indexed=True,
		multiple=True,
		defaultValue=["newsletter", "website"],
		sortBy="values",
		values=conf["project.user.interests"],
		params={
			"tooltip": u"Hier kannst Du einstellen, welche Informationen und Funktionen für Dich relevant sind."
		}
	)

	duties = selectBone(
		descr=u"Dienste",
		indexed=True,
		multiple=True,
		defaultValue=["canteen"],
		values=conf["project.appointment.duties"],
		params={
			"tooltip": u"Hier können Dienste definiert werden, für welche das Mitglied eingeplant werden kann."
		}
	)

	# Segelflug.de Watchkategorien
	segelflugde = relationalBone(
		kind="segelflugde",
		descr=u"Abonnierte Kategorien für segelflug.de WatchDog",
		indexed=True,
		multiple=True,
		params={
			"tooltip": u"""Der segelflug.de WatchDog schickt Dir eine E-Mail wenn's was neues in den von Dir ausgewählten Kategorien gibt.
			<img src="/static/img/arcus-vorm-arcus.jpg" style="width: 100%; border-radius: 15px;">"""
		}
	)

	access = selectAccessBone(
		descr="Access rights",
		values={"root": "Superuser"},
		indexed=True,
	    params={
		    "logic.readonlyIf": "role != 'user'",
	        "category": u"Zugriffsrechte"}
	)

	def fromClient(self, data):
		ret = super(userSkel, self).fromClient(data)

		if ret and "password" in self and data.get("password") and not self.password.readOnly:
			if data["password"] != self["password"]:
				return False

			self["changepassword"] = False

		return ret


	def toDB(self, *args, **kwargs):
		# viewname
		try:
			self["viewname"] = ", ".join([self["lastname"], self["firstname"]])
		except TypeError:
			pass

		# airbatch
		self["airbatch"] = bool(self["airbatch_daec"])

		# role / access
		if self["role"] and self["role"] != "user":
			self["access"] = []

			if self["role"] == "executive":
				self["access"].append("admin")

			for modName in dir(conf["viur.mainApp"]):
				module = getattr(conf["viur.mainApp"], modName)
				roles = getattr(module, "roles", {})
				role = roles.get(self["role"], roles.get("*", []))

				if "*" in role:
					for right in module.accessRights:
						self["access"].append("%s-%s" % (modName, right))
				else:
					for right in role:
						self["access"].append("%s-%s" % (modName, right))

		return super(userSkel, self).toDB(*args, **kwargs)

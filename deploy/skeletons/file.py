# -*- coding: utf-8 -*-
from server.modules.file import fileBaseSkel
from server.bones import *

class fileSkel(fileBaseSkel):
	subSkels = {
		"*": ["name", "parentrepo", "parentdir"],
		"link": ["url", "descr"]
	}

	url = stringBone(
		descr=u"URL",
		params={
			"tooltip": u"Wenn gesetzt, wird dieser Eintrag als Link angezeigt"
		}
	)
	descr = stringBone(descr=u"Beschreibung")

	def preProcessBlobLocks(self, locks):
		if self["dlkey"]:
			locks.add(self["dlkey"])

		return locks

	def toDB(self, *args, **kwargs):
		if not self["kind"] and self["dlkey"]:
			self["kind"] = "file"

		return super(fileSkel, self).toDB(*args, **kwargs)

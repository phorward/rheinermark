# -*- coding: utf-8 -*-
from server.modules.file import File
from server import utils

from skeletons.file import fileSkel

class file(File):
	viewTemplate = "file_view"

	viewLeafSkel = fileSkel
	editLeafSkel = fileSkel
	addLeafSkel = fileSkel

	roles = {
		"*": ["view"]
	}

	def getAvailableRootNodes(self, *args, **kwargs):
		if utils.getCurrentUser():
			repo = self.ensureOwnModuleRootNode()
			res = [{"name": _(u"Dateien"), "key": str(repo.key())}]
			return res

		return []

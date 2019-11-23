# -*- coding: utf-8 -*-
from server.modules.file import File
from server.prototypes.tree import Tree
from server import utils, request
from server import exposed, forceSSL, forcePost

from skeletons.file import fileSkel

class file(File):
	viewTemplate = "file_view"

	roles = {
		"*": ["view"]
	}

	def addLeafSkel(self):
		kind = request.current.get().kwargs.get("kind", "file")
		if kind == "link":
			skel = fileSkel.subSkel("link")
		else:
			skel = fileSkel()

		return skel

	editLeafSkel = viewLeafSkel = fileSkel

	@exposed
	@forceSSL
	@forcePost
	def add(self, *args, **kwargs):
		return super(File, self).add(*args, **kwargs)

	def getAvailableRootNodes(self, *args, **kwargs):
		if utils.getCurrentUser():
			repo = self.ensureOwnModuleRootNode()
			res = [{"name": _(u"Dateien"), "key": str(repo.key())}]
			return res

		return []

# -*- coding: utf-8 -*-
from server.modules.file import File
from server import utils, db, exposed

from skeletons.file import fileSkel

class file(File):

	viewLeafSkel = fileSkel
	editLeafSkel = fileSkel
	addLeafSkel = fileSkel

	def getAvailableRootNodes(self, *args, **kwargs):
		if utils.getCurrentUser():
			repo = self.ensureOwnModuleRootNode()
			res = [{"name": _(u"Dateien"), "key": str(repo.key())}]
			return res

		return []

	@exposed
	def rewriteFiles(self, cursor=None):
		q = self.viewLeafSkel().all()
		q.cursor(cursor)

		repo = self.getAvailableRootNodes()[0]["key"]

		fetched = False
		for skel in q.fetch(limit=99):
			if skel["parentrepo"] != repo:
				if skel["parentdir"] == skel["parentrepo"]:
					skel["parentdir"] = repo

				skel["parentrepo"] = repo
				skel.toDB(clearUpdateTag=True)

			fetched = True

		if fetched:
			self.rewriteFiles(q.getCursor().urlsafe())

	@exposed
	def rewriteDirs(self, cursor=None):
		q = self.viewNodeSkel().all()
		q.cursor(cursor)

		repo = self.getAvailableRootNodes()[0]["key"]

		fetched = False
		for entity in q.run(limit=99):
			if "rootNode" in entity and entity["rootNode"]:
				continue

			if entity["parentrepo"] != repo:
				if entity["parentdir"] == entity["parentrepo"]:
					entity["parentdir"] = repo

				entity["parentrepo"] = repo
				db.Put(entity)

			fetched = True

		if fetched:
			self.rewriteDirs(q.getCursor().urlsafe())

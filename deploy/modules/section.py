# -*- coding: utf-8 -*-
from server.bones import *
from server.prototypes.list import List
from server import errors, securitykey, forceSSL, forcePost, exposed
from server.render.html import default as htmlRenderer

class section(List):
	adminInfo = {

		"name": u"Inhalte",
		"handler": "list",
		"icon": "icons/modules/pages.svg",
		"filter": {"orderby": "sortindex"},
		"preview": "/{{module}}/view/{{key}}",
		"columns": ["sortindex", "online", "alias", "name", "parallax"]
	}

	def listFilter(self, query):
		query = super(section, self).listFilter(query)
		if query:
			if not query.getOrders():
				query.order("sortindex")

			if isinstance(self.render, htmlRenderer):
				query.filter("online", True)

		return query

	@forceSSL
	@forcePost
	@exposed
	def setSortIndex(self, key, index, skey, *args, **kwargs):
		if not securitykey.validate(skey, acceptSessionKey=True):
			raise errors.PreconditionFailed()

		skel = self.editSkel()
		if not skel.fromDB(key):
			raise errors.NotFound()

		skel["sortindex"] = float(index)
		skel.toDB(clearUpdateTag=True)
		return self.render.renderEntry(skel, "setSortIndexSuccess")


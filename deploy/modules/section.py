# -*- coding: utf-8 -*-
from server.bones import *
from prototypes import SortedList
from server import errors, securitykey, forceSSL, forcePost, exposed
from server.render.html import default as HtmlRenderer
import helpers


class section(SortedList):
	roles = {
		"*": ["view"],
		"executive": ["view", "add", "edit"]
	}

	adminInfo = {
		"name": u"Inhalt",
		"handler": "list",
		"mode": "hidden",
		"icon": "icons/modules/pages.svg",
		"filter": {"orderby": "sortindex"},
		"preview": "/{{module}}/view/{{key}}",
		"columns": ["sortindex", "mode", "image", "title", "content"],
	}

	def canAdd(self):
		if not super(section, self).canAdd():
			return False

		return bool(self.addSkel())

	def addSkel(self):
		skel = super(section, self).addSkel()

		page = helpers.getSkelForRequest("page", attr="key")
		if page:
			skel.setBoneValue("page", page)
			return skel

		return None

	def listFilter(self, query):
		page = helpers.getSkelForRequest("page", attr="key")
		if page:
			query.filter("page.dest.key", page)

		if not query.getOrders():
			query.order("sortindex")

		if isinstance(self.render, HtmlRenderer):
			query.filter("online", True)

		return query

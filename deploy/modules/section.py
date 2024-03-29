# -*- coding: utf-8 -*-
from server.bones import *
from prototypes import SortedList
from server import errors, securitykey, forceSSL, forcePost, exposed
from server.render.html import default as HtmlRenderer


class section(SortedList):
	roles = {
		"*": ["view"],
		"executive": ["view", "add", "edit"]
	}

	adminInfo = {
		"name": u"Inhalt",
		"handler": "list",
		"icon": "icons/modules/pages.svg",
		"filter": {"orderby": "sortindex"},
		"preview": "/{{module}}/view/{{key}}",
		"columns": ["sortindex", "online", "alias", "name", "parallax"]
	}

	def listFilter(self, query):
		if query and not query.getOrders():
			query.order("sortindex")

		if isinstance(self.render, HtmlRenderer):
			query.filter("online", True)

		return query

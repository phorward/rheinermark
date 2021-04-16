# -*- coding: utf-8 -*-
from server.bones import *
from prototypes import SortedList
from server.render.html import default as HtmlRenderer


class page(SortedList):
	viewTemplate = "page_view"

	roles = {
		"*": ["view"],
		"executive": ["view", "add", "edit"]
	}

	adminInfo = {
		"name": u"Seite",
		"handler": "list",
		"icon": "icons/modules/pages.svg",
		"preview": "/{{module}}/view/{{key}}",
		"columns": ["sortindex", "online", "alias", "name"],
		"editViews": [
			{
				"module": "section",
				"context": "@page",
				"columns": ["sortindex", "mode", "image", "title", "content"],
				"title": u"Inhalte"
			}
		]
	}

	def listFilter(self, query):
		if not query.getOrders():
			query.order("sortindex")

		if isinstance(self.render, HtmlRenderer):
			query.filter("online", True)

		return query

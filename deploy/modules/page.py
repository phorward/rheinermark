# -*- coding: utf-8 -*-
from server.bones import *
from server import exposed
from prototypes import SortedList
from server.render.html import default as HtmlRenderer
import helpers


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

	@exposed
	def view(self, key, *args, **kwargs):
		q = self.viewSkel().all()
		q.filter("alias", key)
		skel = q.getSkel()
		if skel:
			return self.render.view(skel)

		return super(page, self).view(key, *args, **kwargs)

	def editSkel(self):
		skel = super(page, self).editSkel().ensureIsCloned()

		if not skel.alias.params:
			skel.alias.params = {}

		skel.alias.params = {
			"tooltip":
				u"Definiert einen sprechenden Alias, über den die Seite erreichbar ist, also www.domain.de/alias.\n"
				u"Folgende Aliase sind vom System belegt und dürfen nicht vergeben werden: " + u", ".join(
					helpers.getModuleNames())
		}
		skel.alias.isInvalid = lambda alias: (u"Der Alias '%s' ist bereits vom System vergeben" % alias) if alias in helpers.getModuleNames() else None

		return skel

	addSkel = editSkel

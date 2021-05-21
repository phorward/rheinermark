# -*- coding: utf-8 -*-
from server.bones import *
from prototypes import SortedList
from server import utils
from server.render.html import default as HtmlRenderer
import helpers


class section(SortedList):
	roles = {
		"*": ["view"],
		"executive": ["view", "add", "edit"]
	}

	def adminInfo(self):
		cuser = utils.getCurrentUser()

		return {
			"name": u"Seitenabschnitt ⚠️",
			"handler": "list",
			"mode": "hidden" if not cuser and "root" in cuser["access"] else "normal",
			"icon": "icons/modules/pages.svg",
			"filter": {"orderby": "sortindex"},
			"preview": "/{{module}}/view/{{key}}",
			"columns": ["page", "mode", "image", "title"],
		}

	def addSkel(self):
		skel = super(section, self).addSkel().ensureIsCloned()

		page = helpers.getSkelForRequest("page", attr="key")
		if page:
			skel.page.readOnly = True
			skel.page.visible = False
			skel.setBoneValue("page", page)
		else:
			skel.page.required = True

		return skel

	editSkel = addSkel

	def listFilter(self, query):
		page = helpers.getSkelForRequest("page", attr="key")
		if page:
			query.filter("page.dest.key", page)

		if not query.getOrders():
			query.order("sortindex")

		if isinstance(self.render, HtmlRenderer):
			query.filter("online", True)

		return query

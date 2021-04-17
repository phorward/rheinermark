#-*- coding: utf-8 -*-
from server.prototypes import List
from server.render.html import default as HtmlRenderer
from server import db


class news(List):
	listTemplate = "news_list"
	viewTemplate = "news_view"

	adminInfo = {
		"name": u"Neuigkeiten",
		"handler": "list",
		"icon": "icons/modules/news.svg",
		"filter": {"orderby": "creationdate", "orderdir": "1"},
		"columns": ["date", "title"]
	}

	def listFilter(self, query):
		if not query.getOrders():
			query.order(("date", db.DESCENDING))

		if isinstance(self.render, HtmlRenderer):
			query.filter("online", True)

		return query

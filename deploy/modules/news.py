#-*- coding: utf-8 -*-
from server.prototypes import List
from server.render.html import default as HtmlRenderer


class news(List):
	listTemplate = "news_list"

	adminInfo = {
		"name": u"Neuigkeiten",
		"handler": "list",
		"icon": "icons/modules/news.svg",
		"filter": {"orderby": "creationdate", "orderdir": "1"},
		"columns": ["date", "title"]
	}

	def listFilter(self, query):
		if not query.getOrders():
			query.order("date")

		if isinstance(self.render, HtmlRenderer):
			query.filter("online", True)

		return query

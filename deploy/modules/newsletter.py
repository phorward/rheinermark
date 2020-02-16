# -*- coding: utf-8 -*-
from server.prototypes.list import List
from server import request


class Newsletter(List):
	viewTemplate = "newsletter_view"

	adminInfo = {
		"name": u"Newsletter",
		"handler": "list.place",
		"icon": "icons/modules/newsletter.svg",
		"filter": {"orderby": "creationdate", "orderdir": 1},
		"columns": ["creationdate", "sentdate", "name", "recipients"],
		"preview": "/{{module}}/view/{{key}}"
	}

	roles = {
		"*": ["view"],
		"executive": ["view", "add", "edit", "delete"]
	}

# -*- coding: utf-8 -*-
from server.bones import *
from server.prototypes.list import List
from server import errors, tasks, utils, conf, exposed

from google.appengine.api import app_identity
import requests, re, helpers, logging
from bs4 import BeautifulSoup


class segelflugde(List):
	roles = {
		"*": ["view"]
	}

	adminInfo = {
		"name": u"segelflug.de WatchDog",
		"handler": "list",
		"icon": "/static/img/watchdog-icon.jpg"
	}

	def listFilter(self, query):
		query = super(segelflugde, self).listFilter(query)
		if not query.getOrders():
			query.order("name")

		return query

	@tasks.PeriodicTask(5)
	def watch(self, *args, **kwargs):
		q = self.editSkel().all()
		extractId = re.compile("id=(\d+)")

		for skel in q.fetch(limit=99):
			content = requests.get("https://www.segelflug.de/osclass/index.php?page=search&sCategory=" + skel["category"]).content
			soup = BeautifulSoup(content, "html.parser")

			result = []
			new = []
			for offer in soup.find_all("div", {"class": "listing-attr"}):
				title = offer.find("h4").getText()
				link = offer.find("a")["href"]
				price = offer.find("span", {"class": "currency-value"}).getText()

				id = extractId.search(link).group(1)
				result.append(id)

				if id in (skel["seen"] or []):
					continue

				new.append({
					"title": title,
					"link": link,
					"price": price})

			if new:
				logging.debug("%d new items found", len(new))

				q = conf["viur.mainApp"].user.viewSkel().all()
				q.mergeExternalFilter({
					"segelflugde.dest.key": skel["key"]
				})

				recipients = []
				for userSkel in q.fetch(limit=99):
					recipients.append(userSkel["name"])

				logging.debug("%d recipients found", len(recipients))
				if recipients:
					logging.debug("Sending E-Mail")
					utils.sendEMail(
						"viur@%s.appspotmail.com" % app_identity.get_application_id(),
						"segelflugde",
						{
							"name": skel["name"],
							"items": new
						},
						bcc=recipients
					)

					logging.debug("Updating seen results")
					helpers.setStatus(
						skel["key"],
						{"seen": result}
					)

					logging.debug("Successfully reported %d new items in %r", len(new), skel["name"])
			else:
				logging.debug("No new entries in category %r", skel["name"])

	#@exposed
	#def test(self):
	#	self.watch()

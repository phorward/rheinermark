# -*- coding: utf-8 -*-
from server import conf, utils
from server.modules.formmailer import Formmailer
from skeletons.message import messageSkel

class Message(Formmailer):
	mailTemplate = "message"
	addTemplate = "message_add"
	addSuccessTemplate = "message_add_success"

	def canUse(self):
		return bool(utils.getCurrentUser())

	def getRcpts(self, skel):

		appconf = conf["viur.mainApp"].appconf.getContents()
		assert appconf and appconf["contact_%s" % skel["division"]]

		return appconf["contact_%s" % skel["division"]]

	def mailSkel(self):
		cuser = utils.getCurrentUser()
		assert cuser

		skel = messageSkel()
		skel.setBoneValue("user", cuser["key"])
		return skel


	def getOptions(self, skel):
		cuser = utils.getCurrentUser()
		return {
			"replyTo": cuser["name"]
		}

Message.html = True

# -*- coding: utf-8 -*-
from server.modules.user import User
from server.render.html import default as htmlRender
from server import utils, errors, exposed
from server.tasks import callDeferred
from bones import passwordBone
import logging


class user(User):
	viewTemplate = "user_view"
	addTemplate = "user_add"
	addSuccessTemplate = "user_add_success"
	editTemplate = "user_edit"
	editSuccessTemplate = "user_edit_success"

	def canEdit(self, skel):
		return super(user, self).canView(skel) #All users can edit themself!

	def addSkel(self):
		skel = super(user, self).addSkel()
		skel["password"] = utils.generateRandomString(10)
		skel["changepassword"] = True

		if isinstance(self.render, htmlRender):
			skel = skel.ensureIsCloned()

			skel["role"] = "member"
			skel["status"] = 10

			for name, bone in skel.items():
				if name in ["name", "firstname", "lastname", "airbatch_daec", "interests"]:
					bone.readOnly = False
					bone.visible = True
				else:
					bone.visible = False
					bone.readOnly = True

		return skel

	def editSkel(self):
		skel = super(user, self).editSkel()
		skel.password = passwordBone(descr=u"Passwort", required=False) #scheiss ViUR...

		if isinstance(self.render, htmlRender):
			for name, bone in skel.items():
				if name in ["name", "password", "interests"]:
					bone.readOnly = False
					bone.visible = True
				elif name in []:
					bone.readOnly = True
					bone.visible = True
				else:
					bone.readOnly = True
					bone.visible = False

		return skel

	def onItemAdded(self, skel):
		if skel["password"]:
			self.sendWelcomeMail(str(skel["key"]), skel["password"])

		return super(user, self).onItemAdded(skel)

	@callDeferred
	def sendWelcomeMail(self, key, initial):
		skel = self.viewSkel()
		assert skel.fromDB(key)

		skel["password"] = initial
		#logging.info("initial = %r", initial)

		utils.sendEMail(
			skel["name"],
			"user_welcome",
			skel
		)

	@exposed
	def view(self, key="self", *args, **kwargs):
		try:
			ret =  super(user, self).view(key, *args, **kwargs)
		except errors.Unauthorized:
			if isinstance(self.render, htmlRender):
				raise errors.Redirect("/user/login")

			raise

		return ret

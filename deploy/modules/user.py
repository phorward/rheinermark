# -*- coding: utf-8 -*-
from server.modules.user import User
from server.render.html import default as htmlRender
from server import errors, exposed

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

		if isinstance(self.render, htmlRender):
			skel = skel.ensureIsCloned()

			skel["role"] = "member"
			skel["status"] = 1

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

		if isinstance(self.render, htmlRender):
			skel = skel.ensureIsCloned()

			for name, bone in skel.items():
				if name in ["name", "password", "interests"]:
					bone.readOnly = False
					bone.visible = True
				elif name in ["firstname", "lastname"]:
					bone.readOnly = True
					bone.visible = True
				else:
					bone.readOnly = True
					bone.visible = False

		return skel

	@exposed
	def view(self, key, *args, **kwargs):
		try:
			ret =  super(user, self).view(key, *args, **kwargs)
		except errors.Unauthorized:
			if isinstance(self.render, htmlRender):
				raise errors.Redirect("/user/login")

			raise

		return ret

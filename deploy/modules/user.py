# -*- coding: utf-8 -*-
from server.modules.user import User
from server.render.html import default as htmlRender
from server import errors, exposed

class user(User):
	viewTemplate = "user_view"
	addTemplate = "add"
	addSuccessTemplate = "add_success"

	def addSkel(self):
		skel = super(user, self).addSkel()

		if isinstance(self.render, htmlRender):
			skel = skel.ensureIsCloned()

			skel["role"] = "member"
			skel["status"] = 1

			skel.role.visible = False
			skel.role.readOnly = True

			skel.access.visible = False
			skel.access.readOnly = True

			skel.status.visible = False
			skel.status.readOnly = True

			skel.password.visible = False
			skel.password.readOnly = True

			skel.lastlogin = None
			skel.viewname.visible = False

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

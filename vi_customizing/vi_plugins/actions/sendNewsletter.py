#-*- coding: utf-8 -*-
import html5

from network import NetworkService
from config import conf
from priorityqueue import actionDelegateSelector
from i18n import translate

class SendNewsletterAction(html5.ext.Button):
	def __init__(self, *args, **kwargs):
		super(SendNewsletterAction, self).__init__(translate(u"Newsletter senden"), *args, **kwargs)

	@staticmethod
	def isSuitableFor(module, handler, actionName):
		if module is None or module not in conf["modules"].keys():
			return False

		cuser = conf["currentUser"]
		return actionName == "newsletter.send" and "root" in cuser["access"]

	def onAttach(self):
		super(SendNewsletterAction, self).onAttach()
		self.parent().parent().selectionChangedEvent.register(self)

	def onDetach(self):
		self.parent().parent().selectionChangedEvent.unregister(self)

	def onSelectionChanged(self, table, selection):
		if len(selection) == 1 and selection[0]["triggered"] == False and selection[0]["sent"] == False:
			self.enable()
		else:
			self.disable()

	def onClick(self, sender=None):
		selection = self.parent().parent().getCurrentSelection()
		if not selection:
			return

		html5.ext.YesNoDialog(
			translate(
				u"Möchten Sie den Newsletter '{name}' jetzt verschicken?",
			    name=selection[0]["name"]
			),
			yesCallback=self.onSendNewsletterClick
		)

	def onSendNewsletterClick(self, *args, **kwargs):
		selection = self.parent().parent().getCurrentSelection()
		if not selection:
			return

		self.disable()
		req = NetworkService.request(
			self.parent().parent().module, "triggerSendNewsletter", {
				"key": selection[0]["key"]
			},
			secure=True,
		    successHandler=self.onSendNewsletterSuccess,
		    failureHandler=self.onSendNewsletterFailure
		)
		req.selection = selection[0]

	def onSendNewsletterSuccess(self, req):
		conf["mainWindow"].log(
			"success",
		    translate(
			    u"Versand von '{name}' erfolgreich gestartet!",
		        name=req.selection["name"]
		    )
		)

	def onSendNewsletterFailure(self, req, code):
		if int(code) in [403, 401]:
			conf["mainWindow"].log(
				"error",
				translate(
					u"Sie verfügen nicht über das Recht, diese Funktion auszführen."
				)
			)
		else:
			conf["mainWindow"].log(
				"error",
			    translate(u"Fehler {code}", code=str(code))
			)

actionDelegateSelector.insert(5, SendNewsletterAction.isSuitableFor, SendNewsletterAction)

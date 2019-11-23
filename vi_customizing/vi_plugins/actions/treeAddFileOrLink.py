# -*- coding: utf-8 -*-
import html5
from config import conf
from i18n import translate
from network import NetworkService
from pane import Pane
from priorityqueue import actionDelegateSelector
from widgets.edit import EditWidget

from actions.file import AddLeafAction as FileUploadAction


class AddFileOrLinkAction(html5.Span):

	def __init__(self, *args, **kwargs):
		super(AddFileOrLinkAction, self).__init__()

		self.uploadFile = FileUploadAction()
		self.uploadFile.parent = lambda: self.parent()

		self.createLink = html5.ext.Button(translate("Create link"), callback=self.onClick)
		self.createLink["class"] = "icon add leaf"

		self.appendChild(self.uploadFile)
		self.appendChild(self.createLink)

	@staticmethod
	def isSuitableFor(module, handler, actionName):
		print("XX", module, handler, actionName)

		if module is None or module not in conf["modules"].keys():
			return False

		correctAction = actionName == "add.leaf"
		correctHandler = handler == "tree.simple.file" or handler.startswith("tree.simple.file.")
		hasAccess = conf["currentUser"] and (
				"root" in conf["currentUser"]["access"] or module + "-add" in conf["currentUser"]["access"])
		isDisabled = module is not None and "disabledFunctions" in conf["modules"][module].keys() and \
		             conf["modules"][module]["disabledFunctions"] and "add-leaf" in conf["modules"][module][
			             "disabledFunctions"]

		return correctAction and correctHandler and hasAccess and not isDisabled

	def onClick(self, sender=None):
		pane = Pane("Add", closeable=True,
		            iconClasses=["module_%s" % self.parent().parent().module, "apptype_tree", "action_add_leaf"])
		conf["mainWindow"].stackPane(pane)
		edwg = EditWidget(
			self.parent().parent().module,
			EditWidget.appTree,
			node=self.parent().parent().node,
		    skelType="leaf",
			context={"kind": "link"}
		)

		pane.addWidget(edwg)
		pane.focus()

	def resetLoadingState(self):
		pass


actionDelegateSelector.insert(10, AddFileOrLinkAction.isSuitableFor, AddFileOrLinkAction)

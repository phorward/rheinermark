import html5
from network import NetworkService
from priorityqueue import actionDelegateSelector
from i18n import translate
from config import conf

class ResetPasswordAction(html5.ext.Button):
    def __init__(self, *args, **kwargs):
        super(ResetPasswordAction, self).__init__(translate("Reset password"), *args, **kwargs)
        #self["class"] = "icon kickuser"
        self["disabled"] = True
        self.isDisabled = True

    def onAttach(self):
        super(ResetPasswordAction, self).onAttach()
        self.parent().parent().selectionChangedEvent.register(self)

    def onDetach(self):
        self.parent().parent().selectionChangedEvent.unregister(self)

    def onSelectionChanged(self, table, selection):
        if selection:
            if self.isDisabled:
                self.isDisabled = False
            self["disabled"] = False
        else:
            if not self.isDisabled:
                self["disabled"] = True
                self.isDisabled = True

    @staticmethod
    def isSuitableFor(module, handler, actionName):
        if module is None:
            return False

        if not conf["currentUser"] or not "root" in conf["currentUser"]["access"]:
            return False

        correctAction = actionName == "resetpassword"
        correctHandler = handler == "list.user" or handler.startswith("list.user.")

        return correctAction and correctHandler

    def onClick(self, sender=None):
        selection = self.parent().parent().getCurrentSelection()
        if not selection:
            return

        for s in selection:
            r = NetworkService.request("user", "resetPassword",
                                        params={"key": s["key"]},
                                        successHandler=self.onUserResetSuccess,
                                        failureHandler=self.onUserResetFailure)
            r.dataset = s

    def onUserResetSuccess(self, req):
        conf["mainWindow"].log("success", translate("User '%s' was reset!" % req.dataset["name"]))

    def onUserResetFailure(self, *args, **kwargs):
        print("Failed to reset")

        if "code" in kwargs.keys():
            print("Error code: %s" % kwargs["code"])
        else:
            print("Additional info: %s" % kwargs)

        conf["mainWindow"].log("failure", translate("Unable to reset user!"))

actionDelegateSelector.insert(1, ResetPasswordAction.isSuitableFor, ResetPasswordAction)

print("--- resetpasswordPlugin is up and running ---")

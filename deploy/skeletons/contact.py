# -*- coding: utf-8 -*-
from server.bones import *
from server.skeleton import Skeleton

class contactSkel(Skeleton):
	key = None

	name = stringBone(descr="Ihr Name", required=True)
	email = emailBone(descr="Ihre E-Mail Adresse", required=True)
	descr = textBone(descr="Ihre Nachricht", required=True, validHtml=None)

	privacy_confirm = booleanBone(descr=u"privacy_confirm", required=True)

# -*- coding: utf-8 -*-
from server.modules.file import fileBaseSkel
from server.bones import *

class fileSkel(fileBaseSkel):
	descr = stringBone(descr=u"Beschreibung")

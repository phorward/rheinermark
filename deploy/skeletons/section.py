# -*- coding: utf-8 -*-
import sys
from server.bones import *
from server import conf, skeleton
from time import time


class sectionSkel(skeleton.Skeleton):
	page = relationalBone(
		kind="page",
		descr=u"Seite",
		readOnly=True,
		indexed=True,
		visible=False
	)

	sortindex = numericBone(
		descr="SortIndex",
		indexed=True,
		visible=False,
		readOnly=True,
		mode="float",
		max=sys.maxint
	)

	online = booleanBone(
		descr=u"Online",
		defaultValue=True,
		indexed=True
	)

	mode = selectBone(
		descr=u"Typ",
		values={
			"teaser": u"Teaser",
			"text": u"Text"
		}
	)

	image = fileBone(
		descr=u"Bild"
	)

	title = stringBone(
		descr=u"Titel"
	)

	content = textBone(
		descr=u"Inhalt",
		params={
			"logic.visibleIf": "mode == 'text'"
		}
	)

	def toDB(self, *args, **kwargs):
		if not self["sortindex"]:
			self["sortindex"] = time()

		if self["content"] == "<p><br></p>":
			self["content"] = None

		return super(sectionSkel, self).toDB(*args, **kwargs)

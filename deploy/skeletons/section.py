# -*- coding: utf-8 -*-
import sys
from server.bones import *
from server import conf, skeleton
from time import time
from collections import OrderedDict


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
			"text": u"Text",
			"news": u"News",
			"iframe": u"IFrame"
		},
		defaultValue="text"
	)

	image_position = selectBone(
		descr=u"Bildposition",
		values=OrderedDict([
			("", u"kein Bild"),
			("left", u"links"),
			("right", u"rechts"),
		]),
		defaultValue="",
		params={
			"logic.visibleIf": """ mode == "text" """
		}
	)

	image = fileBone(
		descr=u"Bild",
		params={
			"logic.visibleIf": """ mode == "teaser" or mode == "text" and image_position """
		}
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

	url = stringBone(
		descr=u"Link / URL",
		params={
			"logic.visibleIf": "mode == 'iframe'"
		}
	)

	def toDB(self, *args, **kwargs):
		if not self["sortindex"]:
			self["sortindex"] = time()

		if self["content"] == "<p><br></p>":
			self["content"] = None

		return super(sectionSkel, self).toDB(*args, **kwargs)

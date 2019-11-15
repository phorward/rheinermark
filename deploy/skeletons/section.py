# -*- coding: utf-8 -*-
import sys
from server.bones import *
from server import conf, skeleton
from time import time


class sectionContentSkel(skeleton.RefSkel):
	title = stringBone(
		descr=u"Titel"
	)

	content = textBone(
		descr=u"Inhalt"
	)

	images = fileBone(
		descr=u"Bilder",
		multiple=True
	)

class sectionSkel(skeleton.Skeleton):

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

	# Seite
	alias = stringBone(
		descr=u"Alias",
		unique=u"Dieser Alias ist bereits vergeben!",
		required=True,
		indexed=True,
		params={
			"tooltip": u"Geben Sie bitte eine SEO-freundliche Bezeichnung OHNE Leerzeichen ein!"
		}
	)

	name = stringBone(
		descr=u"Name im Menü",
		indexed=True,
		required=True
	)

	parallax = fileBone(
		descr=u"Parallaxbild"
	)

	content = recordBone(
		descr=u"Inhalte",
		using=sectionContentSkel,
		format="$(title)"
	)

	def toDB(self, *args, **kwargs):
		if not self["sortindex"]:
			self["sortindex"] = time()

		return super(sectionSkel, self).toDB(*args, **kwargs)

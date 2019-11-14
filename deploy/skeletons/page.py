# -*- coding: utf-8 -*-
import sys
from server.bones import *
from server import conf, skeleton
from time import time


class pageContentSkel(skeleton.RefSkel):
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

class pageSkel(skeleton.Skeleton):

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

	online = booleanBone(
		descr=u"Online",
		defaultValue=True,
		indexed=True
	)

	name = stringBone(
		descr=u"Name im Menü",
		indexed=True,
		required=True
	)

	sortindex = numericBone(
		descr="SortIndex",
		indexed=True,
		visible=False,
		readOnly=True,
		mode="float",
		max=sys.maxint
	)

	appearance = selectBone(
		descr=u"Anzeige",
		indexed=True,
		multiple=True,
		required=True,
		values={
			"main": u"Hauptmenü",
			"footer": u"Footer (Allgemein)",
			"footer-icons": u"Footer-Icons"
		},
		defaultValue=["main"]
	)

	icon = fileBone(
		descr=u"Icon",
		params={
			"logic.visibleIf": "'footer-icons' in appearance"
		}
	)

	teaser_headline = stringBone(
		descr=u"Überschrift",
		indexed=True
	)

	teaser_subline = stringBone(
		descr=u"Teaser Untertitel",
		indexed=True
	)

	teaser_image = fileBone(
		descr=u"Teaserbild"
	)

	bodies = recordBone(
		descr=u"Inhalte",
		using=pageContentSkel,
		format="$(title)"
	)

	# SEO
	seo_title = stringBone(descr=u"SEO Title", params={"category": u"SEO"})
	seo_description = stringBone(descr=u"SEO Description", params={"category": u"SEO"})
	seo_keywords = stringBone(descr=u"SEO Keywords", params={"category": u"SEO"})
	seo_author = stringBone(descr=u"SEO Author", params={"category": u"SEO"})
	seo_image = fileBone(descr=u"SEO Vorschaubild", params={"category": u"SEO"})

	def toDB(self, *args, **kwargs):
		if not self["sortindex"]:
			self["sortindex"] = time()

		return super(pageSkel, self).toDB(*args, **kwargs)

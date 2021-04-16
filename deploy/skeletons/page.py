# -*- coding: utf-8 -*-
import sys, os
from server.bones import *
from server.skeleton import Skeleton, RelSkel


class pageSkel(Skeleton):
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
		indexed=True,
		defaultValue=True
	)

	menu = selectBone(
		descr=u"Menü",
		indexed=True,
		multiple=True,
		values={
			"main": u"Hauptmenü",
			"foot": u"Footer"
		},
		defaultValue="main"
	)

	alias = stringBone(
		descr=u"Alias",
		required=True,
		caseSensitive=False,
		indexed=True,
		unique=u"Name muss eindeutig sein!"
	)

	name = stringBone(
		descr=u"Name im Menü",
		required=True
	)

	static = selectBone(
		descr=u"Statischer Inhalt",
		values=[""] + os.listdir("html/sites"),
		defaultValue=""
	)

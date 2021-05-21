# -*- coding: utf-8 -*-
from server.bones import *
from server import conf, skeleton


class segelflugdeSkel(skeleton.Skeleton):

	name = stringBone(
		descr=u"Kategorie",
		required=True,
		searchable=True,
		indexed=True
	)

	category = stringBone(
		descr=u"ID",
		required=True
	)

	seen = stringBone(
		descr=u"Seen",
		readOnly=True,
		visible=False
	)

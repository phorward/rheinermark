# -*- coding: utf-8 -*-
from server.bones import *
from server.skeleton import Skeleton

class appconfSkel(Skeleton):

	# Startseite
	site_title = stringBone(
		descr=u"Seitentitel",
		defaultValue=u"LSV Ruhr-Lenne Iserlohn e.V."
	)

	site_slogan = stringBone(
		descr=u"Seiten-Slogan",
		defaultValue=u"Komm, fliegen!"
	)

	# Start
	start_teaser = fileBone(
		descr=u"Teaser-Bilder",
		required=True,
		multiple=True
	)

	# Formmailer
	contact_rcpts = emailBone(descr=u"Empfänger für Kontaktanfrage", params={"category": "Formmailer"}, required=True)

	# Mitgliederbereich
	intern_document_folders = treeDirBone(
		descr=u"Folder für Mitglieder",
		kind="file",
		multiple=True
	)

	contact_pilots_images = fileBone(
		descr=u"Kontakt - Piloten",
		multiple=True
	)

	# SEO
	seo_title = stringBone(descr=u"SEO Title", params={"category": u"SEO"})
	seo_description = stringBone(descr=u"SEO Description", params={"category": u"SEO"})
	seo_keywords = stringBone(descr=u"SEO Keywords", params={"category": u"SEO"})
	seo_image = fileBone(descr=u"SEO Vorschaubild", params={"category": u"SEO"})

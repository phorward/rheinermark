# -*- coding: utf-8 -*-
from server.bones import *
from server.skeleton import Skeleton

class appconfSkel(Skeleton):

	# Startseite
	site_name = stringBone(
		descr=u"Vollständiger Name des Vereins",
		defaultValue=u"LSV Ruhr-Lenne Iserlohn e.V."
	)

	# Startseite
	site_title = stringBone(
		descr=u"Seitentitel",
		defaultValue=u"LSV Ruhr-Lenne Iserlohn e.V."
	)

	site_slogan = stringBone(
		descr=u"Seiten-Slogan",
		defaultValue=u"Komm, fliegen!"
	)

	# Formmailer
	contact_rcpts = emailBone(
		descr=u"Empfänger für Kontaktanfrage",
		params={"category": "Formmailer"},
		required=True
	)

	contact_executive = emailBone(
		descr=u"Empfänger an Vorstand",
		params={"category": "Formmailer"},
		required=True
	)

	contact_training_glider = emailBone(
		descr=u"Empfänger Schulung - Segelflug",
		params={"category": "Formmailer"},
		required=True
	)
	contact_training_microlight = emailBone(
		descr=u"Empfänger Schulung - Ultraleicht",
		params={"category": "Formmailer"},
	    required=True
	)

	contact_website = emailBone(
		descr=u"Empfänger an Webseite",
		params={"category": "Formmailer"},
		required=True
	)

	# Mitgliederbereich
	intern_document_folders = treeDirBone(
		descr=u"Folder für Mitglieder",
		kind="file",
		multiple=True
	)

	# SEO
	seo_title = stringBone(descr=u"SEO Title", params={"category": u"SEO"})
	seo_description = stringBone(descr=u"SEO Description", params={"category": u"SEO"})
	seo_keywords = stringBone(descr=u"SEO Keywords", params={"category": u"SEO"})
	seo_image = fileBone(descr=u"SEO Vorschaubild", params={"category": u"SEO"})

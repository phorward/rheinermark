# -*- coding: utf-8 -*-
from server.bones import *
from server.skeleton import Skeleton

class appconfSkel(Skeleton):

	# Startseite
	title = stringBone(
		descr=u"Seitentitel",
		defaultValue=u"LSV Ruhr-Lenne Iserlohn e.V."
	)

	slogan = stringBone(
		descr=u"Seiten-Slogan",
		defaultValue=u"Komm, fliegen!"
	)

	# Kontaktdaten
	club = stringBone(descr=u"Club", params={"category": "Kontaktdaten"})
	club_short = stringBone(descr=u"Club (Kurzbezeichnung)", params={"category": "Kontaktdaten"})
	address = stringBone(descr=u"Adresse", params={"category": "Kontaktdaten"})
	zip = stringBone(descr=u"PLZ", params={"category": "Kontaktdaten"})
	city = stringBone(descr=u"Stadt", params={"category": "Kontaktdaten"})

	contact_phone = stringBone(descr=u"Telefon", params={"category": "Kontaktdaten"})
	contact_fax = stringBone(descr=u"Telefax", params={"category": "Kontaktdaten"})
	contact_email = emailBone(descr=u"E-Mail", params={"category": "Kontaktdaten"})

	# Formmailer
	contact_rcpts = emailBone(descr=u"Empfänger für Kontaktanfrage", params={"category": "Formmailer"}, required=True)

	#website = stringBone(descr=u"Website URL")
	# SEO
	seo_title = stringBone(descr=u"SEO Title", params={"category": u"SEO"})
	seo_description = stringBone(descr=u"SEO Description", params={"category": u"SEO"})
	seo_keywords = stringBone(descr=u"SEO Keywords", params={"category": u"SEO"})
	seo_image = fileBone(descr=u"SEO Vorschaubild", params={"category": u"SEO"})

	# Social Media Links
	social_facebook = stringBone(descr=u"Facebook", params={"category": u"Social"})
	social_twitter = stringBone(descr=u"Twitter", params={"category": u"Social"})
	social_instagram = stringBone(descr=u"Instagram", params={"category": u"Social"})

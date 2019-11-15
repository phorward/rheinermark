#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#                 iii
#                iii
#               iii
#
#           vvv iii uu      uu rrrrrrrr
#          vvvv iii uu      uu rr     rr
#   v     vvvv  iii uu      uu rr     rr
#  vvv   vvvv   iii uu      uu rr rrrrr
# vvvvv vvvv    iii uu      uu rr rrr
#  vvvvvvvv     iii uu      uu rr  rrr
#   vvvvvv      iii  uu    uu  rr   rrr
#    vvvv       iii   uuuuuu   rr    rrr
#
#   I N F O R M A T I O N    S Y S T E M
# ------------------------------------------------------------------------------
#
# Project:      rheinermark-viur
# Initiated:    2019-11-14 17:16:31
# Copyright:    Max @ Mausbrand Informationssysteme GmbH
# Author:       Max
#
# ------------------------------------------------------------------------------

from server import conf, securityheaders

# ------------------------------------------------------------------------------
# General configuration
#

#conf["viur.disableCache"] = True

# ------------------------------------------------------------------------------
# Language-specific configuration
#

#conf["viur.languageMethod"] = "url"
#conf["viur.availableLanguages"] = ["en", "de"]

# ------------------------------------------------------------------------------
# ViUR admin tool specific configurations
#

conf["admin.vi.name"] = "rheinermark-viur"
conf["admin.moduleGroups"] = [
	{"prefix":u"Start: ", "name": u"Starterfassung", "icon": "icons/modules/tickets.svg"},
]

# ------------------------------------------------------------------------------
# Content Security Policy

securityheaders.addCspRule("script-src", "unsafe-inline", "enforce")
securityheaders.addCspRule("font-src", "fonts.gstatic.com", "enforce")

# ------------------------------------------------------------------------------
# Server startup
#

import server, modules, render

server.setDefaultLanguage("de") #set default language!
application = server.setup(modules, render)

if __name__ == "__main__":
	server.run()

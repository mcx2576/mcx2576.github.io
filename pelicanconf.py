#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Cecilia Miao'
SITENAME = "Cecilia's Wonderland"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
THEME = "./pelican-themes/pelican-bootstrap3"
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GITHUB_URL = 'http://github.com/mcx2576s'

# Add the search function
DIRECT_TEMPLATES = ('index', 'categories', 'authors','archives', 'search')

# Social widget
SOCIAL = (('github', 'http://github.com/mcx2576'),
        ('facebook', 'https://www.facebook.com/mcx2576'),)

DEFAULT_PAGINATION = False
BOOTSTRAP_THEME = 'sketchy'
PLUGIN_PATHS = ['./plugins/pelican-plugins']
PLUGINS = ['i18n_subsites','render_math','tipue_search.tipue_search']
DISQUS_DISPLAY_COUNTS = True
DISQUS_NO_ID = True
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
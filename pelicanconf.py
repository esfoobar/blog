#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jorge Escobar'
SITENAME = u'JungleG Blog'
SITEURL = 'http://jungleg.com'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'
PATH = 'content' 

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "http://feeds.feedburner.com/jungleg"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),
#           ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/jungleg'),
          ('LinkedIn', 'https://linkedin.com/in/jungleg'),)

DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = 350

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}/index.html"
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

THEME = "/opt/blog/pelican-bootstrap3"
CUSTOM_CSS = 'static/custom.css'
TYPOGRIFY = True

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/favicon.ico',
    'extra/custom.css',
    'extra/common.js'
    ]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/common.js': {'path': 'static/common.js'}
    }

SITELOGO = 'images/logo_final.png'
SITELOGO_SIZE = "100"
HIDE_SITENAME = True

GOOGLE_ANALYTICS_UNIVERSAL = "UA-51840502-1"
GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = "jungleg.com"


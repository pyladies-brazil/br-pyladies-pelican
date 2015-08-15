#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
from datetime import datetime

AUTHOR = u'Pyladies'
SITENAME = u'Pyladies Brasil'
SITEURL = os.environ.get('SITEURL', 'http://localhost:8000')
TAGLINE = u'Ninguém pode fazer você se sentir inferior sem o seu consentimento (Eleanor Roosevelt)'
DEFAULT_DATE_FORMAT = ('%d-%m-%Y')
DEFAULT_BG = 'theme/images/pyladies-avatar.png'
SINCE = datetime.now().year
SUMMARY_MAX_LENGTH = 30
# ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'

# Sitemap
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'


TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = u'en'
THEME = 'themes/default'

PATH = 'content'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (
    ('Sobre', '/about/'),
    ('Blog', '/blog/'),
    ('Eventos', '/events/'),
    ('Locais', '/locations/'),
    ('Ladies', '/ladies/'),
)

DEFAULT_PAGINATION = 10

# ANALYTICS
GOOGLE_ANALYTICS_UA = 'UA-58961512-1'

DISQUS_SITENAME = 'pyladiesbrasil'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

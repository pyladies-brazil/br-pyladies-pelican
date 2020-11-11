#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
from collections import namedtuple

import os
import yaml

AUTHOR = u'Pyladies'
SITENAME = u'Pyladies Brasil'
SITEURL = '{}'.format(os.getenv('SITEURL', 'http://localhost:{}'.format(os.getenv('PORT', '8000'))))
TAGLINE = (u'Ninguém pode fazer você se sentir inferior'
           'sem o seu consentimento (Eleanor Roosevelt)')
DEFAULT_DATE_FORMAT = ('%d-%m-%Y')
DEFAULT_BG = 'images/marca/logo-oficial-pyladies-brasil-cabeca-sem-borda.png'
SINCE = datetime.now().year
NOW = datetime.now().date()
SUMMARY_MAX_LENGTH = 30

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{}index.html'.format(ARTICLE_URL)

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

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
    ('Sobre', '/about'),
    ('Locais', '/locations'),
    ('Videos', '/videos'),
    ('Materiais', '/materiais'),
    ('Blog', '/archives.html'),
)

DEFAULT_PAGINATION = 10

READERS = {'html': None}

STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/favicon.ico',
    'extra/favicon.png',
    # Site estático da primeira edição do evento
    'conf-1',
    # Site estático da primeira edição da PyLadies Conf Nordeste
    'conf-nordeste-1'
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon.png': {'path': 'favicon.png'},
    'conf-1': {'path': 'conf-1'},
    'conf-nordeste-1': {'path': 'conf-nordeste-1'},
}

# ANALYTICS
GOOGLE_ANALYTICS_UA = 'UA-58961512-1'

DISQUS_SITENAME = 'pyladiesbrasil'
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


# Locations, Events and Videos

with open('data/locations.yml') as locations:
    locations_converted = yaml.safe_load(locations.read())
    LOCATIONS = []
    for location in locations_converted:
        LOCATIONS.append(
            namedtuple('Locations', location.keys())(**location)
        )
        
if os.path.isfile("data/videos_depo.yml"):
    with open("data/videos_depo.yml") as videos:
        videos_converted = yaml.safe_load(videos.read())
        VIDEOS_DEPO = [
            namedtuple("Videos", video.keys())(**video)
            for video in videos_converted
            if video["url"]
        ]

if os.path.isfile("data/videos_dojos.yml"):
    with open("data/videos_dojos.yml") as videos:
        videos_converted = yaml.safe_load(videos.read())
        VIDEOS_DOJOS = [
            namedtuple("Videos", video.keys())(**video)
            for video in videos_converted
            if video["url"]
        ]

if os.path.isfile("data/videos_talks.yml"):
    with open("data/videos_talks.yml") as videos:
        videos_converted = yaml.safe_load(videos.read())
        VIDEOS_TALKS = [
            namedtuple("Videos", video.keys())(**video)
            for video in videos_converted
            if video["url"]
        ]

if os.path.isfile("data/videos_tutorials.yml"):
    with open("data/videos_tutorials.yml") as videos:
        videos_converted = yaml.safe_load(videos.read())
        VIDEOS_TUTORIALS = [
            namedtuple("Videos", video.keys())(**video)
            for video in videos_converted
            if video["url"]
        ]

with open('data/talks.yml') as talks:
    talks_readed = yaml.safe_load(talks.read())
    TALKS = []
    for talk in talks_readed:
        TALKS.append(
            namedtuple('Talks', talk.keys())(**talk)
        )

with open('data/materials.yml') as materials:
    materials_readed = yaml.safe_load(materials.read())
    MATERIALS = []
    for materials in materials_readed:
        MATERIALS.append(
            namedtuple('Materials', materials.keys())(**materials)
        )

PLUGIN_PATHS = ['plugins']
PLUGINS = ['tipue_search']

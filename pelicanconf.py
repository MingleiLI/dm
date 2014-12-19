#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ray Alez'
SITENAME = 'digitalmind'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = [
    'static/.htaccess',
    'static/CNAME',    
    ]


TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Menu
MENUITEMS = [('Home', '/'), ('Articles', '/')]

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
ARTICLE_URL = 'post/{slug}'
ARTICLE_SAVE_AS = 'post/{slug}.html'
PAGE_URL = '{slug}' 
PAGE_SAVE_AS = '{slug}.html'

TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

THEME = "/home/ray/projects/digitalmind/themes/digitalmind"

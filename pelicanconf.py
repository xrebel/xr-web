#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "XR"
SITENAME = "Extinction Rebellion Deutschland"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/Berlin"

DEFAULT_LANG = "de"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "http://getpelican.com/"),
    ("Python.org", "http://python.org/"),
    ("Jinja2", "http://jinja.pocoo.org/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (("You can add links in your config file", "#"), ("Another social link", "#"))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "themes/extinctionrebellion.de"

STATIC_PATHS = ["extra"]

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["assets"]

EXTRA_PATH_METADATA = {
    "extra/android-chrome-192x192.png": {"path": "android-chrome-192x192.png"},
    "extra/android-chrome-512x512.png": {"path": "android-chrome-512x512.png"},
    "extra/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
    "extra/browserconfig.xml": {"path": "browserconfig.xml"},
    "extra/favicon-16x16.png": {"path": "favicon-16x16.png"},
    "extra/favicon-32x32.png": {"path": "favicon-32x32.png"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/mstile-144x144.png": {"path": "mstile-144x144.png"},
    "extra/mstile-150x150.png": {"path": "mstile-150x150.png"},
    "extra/mstile-310x150.png": {"path": "mstile-310x150.png"},
    "extra/mstile-310x310.png": {"path": "mstile-310x310.png"},
    "extra/mstile-70x70.png": {"path": "mstile-70x70.png"},
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/safari-pinned-tab.svg": {"path": "safari-pinned-tab.svg"},
    "extra/site.webmanifest": {"path": "site.webmanifest"},
}

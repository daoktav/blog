#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "daoktav"
SITENAME = "DaOktav"
SITEURL = ""

STATIC_PATHS = ["theme/images", "images", "cv"]
TIMEZONE = "Asia/Jakarta"
DATE_FORMATS = {"en": "%b %d, %Y"}
DEFAULT_LANG = "en"

# Plugins and extensions
PLUGIN_PATHS = ["plugins/"]
PLUGINS = [
    "extract_toc",
    "neighbors",
    "render_math",
    "related_posts",
    "tipue_search",
    "liquid_tags.img",
    "render_math",
    "assets",
    "series",
    "sitemap",
    "post_stats",
]

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

# TOC Setting
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.toc": {"title": "Table of contents:"},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}

# Appearance
TYPOGRIFY = True
THEME = "../elegant"
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_CATEGORY = "Miscellaneous"
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = "{slug}"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social
SOCIAL = ("Twitter", "http://twitter.com/raghdaso")

DIRECT_TEMPLATES = ("index", "tags", "categories", "archives", "search", "404")
TAG_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
USE_SHORTCUT_ICONS = True

SOCIAL_PROFILE_LABEL = "Stay in Touch"
RELATED_POSTS_LABEL = "Keep Reading"
COMMENTS_INTRO = "So what do you think ?  Leave your comments below."

FAVOURITE_SYMBOL = "🌟"

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

########################################
# Configuration, please edit
# https://getnikola.com/conf.html
########################################

# post_pages contains (wildcard, destination, template, use_in_feed) tuples.
#
# The wildcard is used to generate a list of reSt source files (whatever/thing.txt)
# That fragment must have an associated metadata file (whatever/thing.meta),
# and opcionally translated files (example for spanish, with code "es"):
#     whatever/thing.txt.es and whatever/thing.meta.es
#
# From those files, a set of HTML fragment files will be generated:
# whatever/thing.html (and maybe whatever/thing.html.es)
#
# These files are combinated with the template to produce rendered
# pages, which will be placed at
# output / TRANSLATIONS[lang] / destination / pagename.html
#
# where "pagename" is specified in the metadata file.
#
# if use_in_feed is True, then those posts will be added to the site's
# rss feeds.
#

POSTS = (
    ("posts/*.txt", "blog", "post.tmpl"),
    ("posts/*.rst", "blog", "post.tmpl"),
    ("posts/*.md", "blog", "post.tmpl"),
    ("posts/*.html", "blog", "post.tmpl"),
    ("posts/*.ipynb","blog","post.tmpl")
)

PAGES = (
    ("stories/*.txt", "", "story.tmpl"),
    ("stories/*.rst", "", "story.tmpl"),
    ("stories/*.html", "", "story.tmpl"),
    ("stories/*.md", "", "story.tmpl")

)

SHOW_SOURCELINK=False
# show_source_link=False
# What is the default language?

DEFAULT_LANG = "en"

# What languages do you have?
# If a specific post is not translated to a language, then the version
# in the default language will be shown instead.
# The format is {"translationcode" : "path/to/translation" }
# the path will be used as a prefix for the generated pages location

TRANSLATIONS = {
    "en": "",
    }

# Paths for different autogenerated bits. These are combined with the translation
# paths.

# Final locations are:
# output / TRANSLATION[lang] / TAG_PATH / index.html (list of tags)
# output / TRANSLATION[lang] / TAG_PATH / tag.html (list of posts for a tag)
# output / TRANSLATION[lang] / TAG_PATH / tag.xml (RSS feed for a tag)
TAG_PATH = "categories"
# Final location is output / TRANSLATION[lang] / INDEX_PATH / index-*.html
INDEX_PATH = "blog"
# Final locations for the archives are:
# output / TRANSLATION[lang] / ARCHIVE_PATH / archive.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / index.html
# ARCHIVE_PATH = "archive"
# Final locations are:
# output / TRANSLATION[lang] / RSS_PATH / rss.xml
RSS_PATH = ""

# INPUT_FORMAT = "rest"
PRETTY_URLS = False
# A list of redirection tuples, [("foo/from.html", "/bar/to.html")].
#
# A HTML file will be created in output/foo/from.html that redirects
# to the "/bar/to.html" URL. notice that the "from" side MUST be a
# relative URL.
#
# If you don't need any of these, just set to []

REDIRECTIONS = []

# Commands to execute to deploy. Can be anything, for example,
# you may use rsync:
# "rsync -rav output/* joe@my.site:/srv/www/site"
# And then do a backup, or ping pingomatic.
# To do manual deployment, set it to []



SHOW_BLOG_TITLE = True

##############################################################################
# Image Gallery Options
##############################################################################

GALLERY_FOLDERS = {'galleries': 'galleries'}
# THUMBNAIL_SIZE = 180

# MAX_IMAGE_SIZE = 5000

# WRITE_TAG_CLOUD = True

##############################################################################
# HTML fragments and diverse things that are used by the templates
##############################################################################

# Data about this site
BLOG_TITLE = "Hello world"
# SITE_URL = "https://getnikola.com/"
# BLOG_EMAIL = "info@getnikola.com"
# BLOG_DESCRIPTION = "A blog about Nikola, the static website generator."
BLOG_AUTHOR = "Jonathan Barrios"

# A HTML fragment describing the license, for the sidebar.
# I recomment using Creative Commons' wizard: http://creativecommons.org/choose/
LICENSE = """
    <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/2.5/ar/">
    <img alt="Creative Commons License" style="border-width:0; margin-bottom:12px;"
    src="https://i.creativecommons.org/l/by-nc-sa/2.5/ar/88x31.png"></a>"""

# A small copyright notice for the page footer
# CONTENT_FOOTER = '''Contents © 2012–2020 <a href="/contact.html">Roberto Alsina and the Nikola contributors</a>&nbsp;&nbsp;|&nbsp;&nbsp;Powered by Nikola itself&nbsp;&nbsp;|&nbsp;&nbsp;
# <a href="https://twitter.com/intent/user?screen_name=GetNikola">Follow Nikola on Twitter</a>&nbsp;&nbsp;|&nbsp;&nbsp;Theme is <a href="https://bootswatch.com/cerulean/">Cerulean</a>
# '''

# TWITTER_CARD = {
#     'use_twitter_cards': True,  # enable Twitter Cards
#     'site': '@GetNikola',  # twitter nick for the website
# }

# To enable comments via Disqus, you need to create a forum at http://disqus.com,
# and set DISQUS_FORUM to the short name you selected.
# If you want to disable comments, set it to False.
# COMMENT_SYSTEM = "disqus"
# COMMENT_SYSTEM_ID = "nikolaweb"

# RSS_LINK is a HTML fragment to link the RSS or Atom feeds. If set to None,
# the base.tmpl will use the feed Nikola generates. However, you may want to
# change it for a feedburner feed or something else.

#RSS_LINK = """
    #<link rel="alternate" type="application/rss+xml" title="RSS" href="http://feeds.feedburner.com/LateralOpinion">
    #<link rel="alternate" type="application/rss+xml" title="RSS en Espanol" href="http://feeds.feedburner.com/LateralOpinionEsp">
#"""
RSS_LINK = None
MATHJAX_CONFIG = """
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    tex2jax: {
        inlineMath: [ ['$','$'], ["\\\(","\\\)"] ],
        displayMath: [ ['$$','$$'], ["\\\[","\\\]"] ],
        processEscapes: true
    },
    displayAlign: 'center', // Change this to 'left' if you want left-aligned equations.
    "HTML-CSS": {
        styles: {'.MathJax_Display': {"margin": 0}}
    }
});
</script>
"""
# A search form to search this site, for the sidebar. You can use a google
# custom search (http://www.google.com/cse/)
# Or a duckduckgo search: https://duckduckgo.com/search_box.html
# This example should work for pretty much any site we generate.
SEARCH_FORM = """ """
ENGINE="jinja"
# THEME_COLOR = "#f5ab14"
THEME="custom"
# Google analytics or whatever else you use. Added to the bottom of <body>
# in the default template (base.tmpl).
#BODY_END = 

# no addthis
SOCIAL_BUTTONS_CODE = ''

NAVIGATION_LINKS={
    DEFAULT_LANG :((('/blog/index.html','BLOG')))
}

# Locale-dependent links for the sidebar
NAVIGATION_LINKS = {
    DEFAULT_LANG: (

        ('/blog/index.html', 'Blog'),
        ('/my-first-page.html','Pages')
    ),
}

EXTRA_HEAD_DATA = ''

CODE_COLOR_SCHEME = 'monokai'
# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.
GLOBAL_CONTEXT = {}

GZIP_FILES = False
IMAGE_FOLDERS = {'images': 'images'}
IMAGE_THUMBNAIL_SIZE = 400

from nikola import filters
FILTERS = {
    ".html": [filters.add_header_permalinks, filters.deduplicate_ids]
}

HEADER_PERMALINKS_FILE_BLACKLIST = ['output/index.html']

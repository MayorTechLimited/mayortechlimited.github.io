AUTHOR = "William Mayor"
SITENAME = "MayorTech Limited"
SITEURL = ""
STATIC_PATHS = ["images"]

PATH = "content"
ARTICLE_PATHS = ["blog"]
ARTICLE_URL = "blog/{slug}/"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"
PAGE_PATHS = [""]
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

TIMEZONE = "Europe/London"

DEFAULT_LANG = "en"

THEME = "./theme"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

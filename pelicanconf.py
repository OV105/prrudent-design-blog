AUTHOR = 'Timothy Lee'
SITENAME = 'Prudent Design'
SITETITLE = 'Prudent Design'
SITESUBTITLE = 'A blog by Timothy Lee'
SITEURL = ''
THEME = 'Flex'
SITELOGO = SITEURL + "/images/head_shot_4_circle.jpg"
PATH = 'content'
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"
TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = True
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)
# Blogroll
LINKS = (('icechest', 'https://github.com/OV105/icechest/tree/MVP'),
	 ('Korea trip', 'http://korea2023trip-to-legacy.s3-website-us-east-1.amazonaws.com'),)

# Social widget
SOCIAL = (
    ("linkedin", "https://linkedin.com/in/timhlee"),
    ("github", "https://github.com/ov105"),
)
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

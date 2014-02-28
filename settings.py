# Scrapy settings for livingS project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'boxOffice'
#LOG_LEVEL = 'CRITICAL'
AUTOTHROTTLE_ENABLED = True 
COOKIES_ENABLED = True
COOKIES_DEBUG = True

SPIDER_MODULES = ['boxOffice.spiders']
NEWSPIDER_MODULE = 'boxOffice.spiders'
ITEM_PIPELINES = ['boxOffice.pipelines.boxOfficePipeline']
DATABASE ={'drivername':'postgres',
'host':'localhost',
'port':'5432',
'username':'',
'password':'',
'database':'scrape'}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'livingS (+http://www.yourdomain.com)'

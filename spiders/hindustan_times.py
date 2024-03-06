from typing import Iterable
import scrapy

from items.news_items import NewsItems
from scrapy.exceptions import IgnoreRequest


class HTSpider(scrapy.Spider):
    name = 'hindustan_times'
    allowed_domains = ['hindustantimes.com']
    base_url = 'https://www.hindustantimes.com/'

    custom_settings = {
        'ROBOTSTXT_OBEY' : False
    }

        
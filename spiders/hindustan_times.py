from typing import Iterable
import scrapy
import pika
from rmq import RMQConnection

from items.news_items import NewsItems
from scrapy.exceptions import IgnoreRequest


class HTSpider(scrapy.Spider):
    name = 'hindustan_times'
    allowed_domains = ['hindustantimes.com']
    base_url = 'https://www.hindustantimes.com/'

    custom_settings = {
        'ROBOTSTXT_OBEY' : False
    }
    start_urls = [base_url]

    def __init__(self, *args, **kwargs):
        super(HTSpider, self).__init__(*args, **kwargs)
        self.rmq = RMQConnection(queue_name='news_queue')

    def parse(self, response):
        try:
            articles = response.css('div.storyShortDetail')
            if not articles:
                raise IgnoreRequest("No articles found on the page")
            for article in articles:
                item = NewsItems()
                item['title'] = article.css('h2 a::text').get()
                item['link'] = article.css('h2 a::attr(href)').get()
                item['summary'] = article.css('div.sortDec::text').get()
                yield item
                self.send_to_queue(item)

            next_page = response.css('a.next::attr(href)').get()
            if next_page:
                yield response.follow(next_page, self.parse)
        except Exception as e:
            self.logger.error(f"Error parsing response: {e}")
            raise IgnoreRequest(f"Error parsing response: {e}")

    def send_to_queue(self, item):
        try:
            self.rmq.publish_message(str(item))
        except Exception as e:
            self.logger.error(f"Error sending to queue: {e}")

    def close(self, reason):
        self.rmq.close_connection()
        super(HTSpider, self).close(reason)

import scrapy
from rmq import RMQConnection
from scrapy.exceptions import IgnoreRequest

class TheMintSpider(scrapy.Spider):
    name = "themint"
    allowed_domains = ["themint.org"]
    start_urls = ["https://www.themint.org/"]

    def __init__(self, *args, **kwargs):
        super(TheMintSpider, self).__init__(*args, **kwargs)
        self.rmq = RMQConnection(queue_name='news_queue')

    def parse(self, response):
        try:
            articles = response.css('div.article')
            if not articles:
                raise IgnoreRequest("No articles found on the page")
            for article in articles:
                item = {
                    'title': article.css('h2::text').get(),
                    'link': article.css('a::attr(href)').get(),
                }
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
        super(TheMintSpider, self).close(reason)
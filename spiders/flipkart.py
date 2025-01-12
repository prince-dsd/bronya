import scrapy
from rmq import RMQConnection

class FlipkartSpider(scrapy.Spider):
    name = "flipkart"
    start_urls = ['https://www.flipkart.com/']

    def __init__(self, *args, **kwargs):
        super(FlipkartSpider, self).__init__(*args, **kwargs)
        self.rmq = RMQConnection(queue_name='flipkart_queue')

    def parse(self, response):
        # Example parsing logic
        for product in response.css('div._1AtVbE'):
            item = {
                'title': product.css('a.IRpwTa::text').get(),
                'price': product.css('div._30jeq3::text').get(),
                'link': product.css('a::attr(href)').get(),
            }
            self.send_to_queue(item)
            yield item

    def send_to_queue(self, item):
        try:
            self.rmq.publish_message(str(item))
        except Exception as e:
            self.logger.error(f"Error sending to queue: {e}")

    def close(self, reason):
        self.rmq.close_connection()
        super(FlipkartSpider, self).close(reason)
import scrapy
from rmq import RMQConnection
from scrapy.exceptions import IgnoreRequest
from models.screener_in_item import ScreenerInItem
from utils.screener_in_selectors import ScreenerInSelectors

class ScreenerInSpider(scrapy.Spider):
    name = "screener_in"
    allowed_domains = ["screener.in"]
    start_urls = ['https://www.screener.in/screens/']
    
    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'DOWNLOAD_DELAY': 3,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    def __init__(self, *args, **kwargs):
        super(ScreenerInSpider, self).__init__(*args, **kwargs)
        self.rmq = RMQConnection(queue_name='screener_in_queue')

    def parse(self, response):
        try:
            rows = response.css('table.data-table tbody tr')
            
            for row in rows:
                item = self.extract_item(row)
                self.send_to_queue(item.dict())
                yield item.dict()

            next_page = response.css('a.next::attr(href)').get()
            if next_page:
                yield response.follow(next_page, self.parse)

        except Exception as e:
            self.logger.error(f"Error parsing response: {e}")
            raise IgnoreRequest(f"Error parsing response: {e}")

 

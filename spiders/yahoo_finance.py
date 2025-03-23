from typing import Iterable
import scrapy
from scrapy.exceptions import IgnoreRequest
from services.stock_service import StockService
from items.stock_items import StockItems

class YahooFinanceSpider(scrapy.Spider):
    name = 'yahoo_finance'
    allowed_domains = ['finance.yahoo.com']
    base_url = 'https://finance.yahoo.com/quote/'

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'DOWNLOAD_DELAY': 2,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1
    }

    def __init__(self, symbols=None, *args, **kwargs):
        super(YahooFinanceSpider, self).__init__(*args, **kwargs)
        self.stock_service = StockService()
        self.symbols = symbols.split(',') if symbols else ['AAPL', 'GOOGL', 'MSFT']

    def start_requests(self):
        for symbol in self.symbols:
            url = f"{self.base_url}{symbol}"
            yield scrapy.Request(url, callback=self.parse, meta={'symbol': symbol})

    def parse(self, response):
        try:
            symbol = response.meta['symbol']
            item = self.stock_service.extract_stock_data(response, symbol)
            self.stock_service.send_to_queue(item)
            yield item

        except Exception as e:
            self.logger.error(f"Error parsing response for {symbol}: {e}")
            raise IgnoreRequest(f"Error parsing response: {e}")

    def close(self, reason):
        self.stock_service.close_connection()
        super(YahooFinanceSpider, self).close(reason)
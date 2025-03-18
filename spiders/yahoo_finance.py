from typing import Iterable
import scrapy
from decimal import Decimal
from items.stock_items import StockItems
from scrapy.exceptions import IgnoreRequest
from rmq import RMQConnection

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
        self.rmq = RMQConnection(queue_name='stock_queue')
        self.symbols = symbols.split(',') if symbols else ['AAPL', 'GOOGL', 'MSFT']

    def start_requests(self):
        for symbol in self.symbols:
            url = f"{self.base_url}{symbol}"
            yield scrapy.Request(url, callback=self.parse, meta={'symbol': symbol})

    def parse(self, response):
        try:
            item = StockItems()
            
            # Basic Information
            item['symbol'] = response.meta['symbol']
            item['company_name'] = response.css('h1::text').get()
            item['exchange'] = response.css('.exchange::text').get()
            
            # Price Information
            price_section = response.css('.quote-header-section')
            item['current_price'] = self.extract_decimal(price_section.css('.Fw\\(b\\)::text').get())
            item['price_change'] = self.extract_decimal(price_section.css('.Fz\\(24px\\)::text').get())
            
            # Market Data
            market_data = response.css('.quote-summary-details')
            item['market_cap'] = self.extract_decimal(market_data.css('[data-test="MARKET_CAP-value"]::text').get())
            item['pe_ratio'] = self.extract_decimal(market_data.css('[data-test="PE_RATIO-value"]::text').get())
            
            yield item
            self.send_to_queue(item)

        except Exception as e:
            self.logger.error(f"Error parsing response for {response.meta['symbol']}: {e}")
            raise IgnoreRequest(f"Error parsing response: {e}")

    def extract_decimal(self, value):
        if not value:
            return None
        try:
            return Decimal(value.replace(',', ''))
        except:
            return None

    def send_to_queue(self, item):
        try:
            self.rmq.publish_message(str(item))
        except Exception as e:
            self.logger.error(f"Error sending to queue: {e}")

    def close(self, reason):
        self.rmq.close_connection()
        super(YahooFinanceSpider, self).close(reason)
import scrapy
from rmq import RMQConnection
from scrapy.exceptions import IgnoreRequest
from models.screener_item import ScreenerItem
from utils.screener_selectors import ScreenerSelectors

class ScreenerSpider(scrapy.Spider):
    name = "screener"
    allowed_domains = ["finviz.com"]
    start_urls = ['https://finviz.com/screener.ashx']
    
    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'DOWNLOAD_DELAY': 2,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1
    }

    def __init__(self, *args, **kwargs):
        super(ScreenerSpider, self).__init__(*args, **kwargs)
        self.rmq = RMQConnection(queue_name='screener_queue')

    def parse(self, response):
        try:
            rows = response.css('table.screener_table tr[valign="top"]')
            
            for row in rows:
                item = self.extract_item(row)
                self.send_to_queue(item.dict())
                yield item.dict()

            # Handle pagination if needed
            next_page = response.css('a.screener-pages:contains("next")::attr(href)').get()
            if next_page:
                yield response.follow(next_page, self.parse)

        except Exception as e:
            self.logger.error(f"Error parsing response: {e}")
            raise IgnoreRequest(f"Error parsing response: {e}")

    def extract_item(self, row):
        def extract_data(selector):
            return row.css(selector).get('').strip()

        return ScreenerItem(
            symbol=extract_data(ScreenerSelectors.SYMBOL),
            company_name=extract_data(ScreenerSelectors.COMPANY_NAME),
            market_cap=extract_data(ScreenerSelectors.MARKET_CAP),
            pe_ratio=extract_data(ScreenerSelectors.PE_RATIO),
            price=extract_data(ScreenerSelectors.PRICE),
            volume=extract_data(ScreenerSelectors.VOLUME),
            sector=extract_data(ScreenerSelectors.SECTOR),
            industry=extract_data(ScreenerSelectors.INDUSTRY),
            dividend_yield=extract_data(ScreenerSelectors.DIVIDEND_YIELD),
            eps=extract_data(ScreenerSelectors.EPS),
            beta=extract_data(ScreenerSelectors.BETA),
            high_52_week=extract_data(ScreenerSelectors.HIGH_52_WEEK),
            low_52_week=extract_data(ScreenerSelectors.LOW_52_WEEK),
            moving_avg_50d=extract_data(ScreenerSelectors.MOVING_AVG_50D),
            moving_avg_200d=extract_data(ScreenerSelectors.MOVING_AVG_200D),
            relative_volume=extract_data(ScreenerSelectors.RELATIVE_VOLUME),
            change_percent=extract_data(ScreenerSelectors.CHANGE_PERCENT)
        )

    def send_to_queue(self, item):
        try:
            self.rmq.publish_message(str(item))
        except Exception as e:
            self.logger.error(f"Error sending to queue: {e}")

    def close(self, reason):
        self.rmq.close_connection()
        super(ScreenerSpider, self).close(reason)

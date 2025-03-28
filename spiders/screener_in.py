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

    def extract_item(self, row):
        def extract_data(selector):
            return row.css(selector).get('').strip()

        return ScreenerInItem(
            symbol=extract_data(ScreenerInSelectors.SYMBOL),
            company_name=extract_data(ScreenerInSelectors.COMPANY_NAME),
            market_cap=extract_data(ScreenerInSelectors.MARKET_CAP),
            current_price=extract_data(ScreenerInSelectors.CURRENT_PRICE),
            high_price=extract_data(ScreenerInSelectors.HIGH_PRICE),
            low_price=extract_data(ScreenerInSelectors.LOW_PRICE),
            pe_ratio=extract_data(ScreenerInSelectors.PE_RATIO),
            book_value=extract_data(ScreenerInSelectors.BOOK_VALUE),
            dividend_yield=extract_data(ScreenerInSelectors.DIVIDEND_YIELD),
            roce=extract_data(ScreenerInSelectors.ROCE),
            roe=extract_data(ScreenerInSelectors.ROE),
            face_value=extract_data(ScreenerInSelectors.FACE_VALUE),
            sector=extract_data(ScreenerInSelectors.SECTOR),
            profit_growth=extract_data(ScreenerInSelectors.PROFIT_GROWTH),
            sales_growth=extract_data(ScreenerInSelectors.SALES_GROWTH),
            promoter_holding=extract_data(ScreenerInSelectors.PROMOTER_HOLDING),
            debt_to_equity=extract_data(ScreenerInSelectors.DEBT_TO_EQUITY),
            working_capital=extract_data(ScreenerInSelectors.WORKING_CAPITAL)
        )


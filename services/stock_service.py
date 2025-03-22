from decimal import Decimal
from typing import Optional, Dict, Any
from items.stock_items import StockItems
from rmq import RMQConnection

class StockService:
    def __init__(self, queue_name: str = 'stock_queue'):
        self.rmq = RMQConnection(queue_name=queue_name)

    def extract_stock_data(self, response: Any, symbol: str) -> StockItems:
        """Extract stock data from response and create StockItems object"""
        item = StockItems()
        
        # Basic Information
        item['symbol'] = symbol
        item['company_name'] = response.css('h1::text').get()
        item['exchange'] = response.css('.exchange::text').get()
        
        # Price Information
        price_section = response.css('.quote-header-section')
        item['current_price'] = self._extract_decimal(price_section.css('.Fw\\(b\\)::text').get())
        item['price_change'] = self._extract_decimal(price_section.css('.Fz\\(24px\\)::text').get())
        
        # Market Data
        market_data = response.css('.quote-summary-details')
        item['market_cap'] = self._extract_decimal(market_data.css('[data-test="MARKET_CAP-value"]::text').get())
        item['pe_ratio'] = self._extract_decimal(market_data.css('[data-test="PE_RATIO-value"]::text').get())
        
        return item

    def send_to_queue(self, item: StockItems) -> None:
        """Send stock data to RabbitMQ queue"""
        self.rmq.publish_message(str(item))

    def close_connection(self) -> None:
        """Close RabbitMQ connection"""
        self.rmq.close_connection()

    @staticmethod
    def _extract_decimal(value: Optional[str]) -> Optional[Decimal]:
        """Convert string value to Decimal"""
        if not value:
            return None
        try:
            return Decimal(value.replace(',', ''))
        except:
            return None
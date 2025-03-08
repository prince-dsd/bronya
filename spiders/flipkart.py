import scrapy
from rmq import RMQConnection
from models.flipkart_item import FlipkartItem
from utils.flipkart_selectors import FlipkartSelectors

class FlipkartSpider(scrapy.Spider):
    name = "flipkart"
    start_urls = ['https://www.flipkart.com/']

    def __init__(self, *args, **kwargs):
        super(FlipkartSpider, self).__init__(*args, **kwargs)
        self.rmq = RMQConnection(queue_name='flipkart_queue')

    def parse(self, response):
        # Example parsing logic
        for product in response.css('div._1AtVbE'):
            item = self.extract_item(product, response)
            self.send_to_queue(item.dict())
            yield item.dict()

    def extract_item(self, product, response):
        def extract_data(selector, method='get', regex=None):
            if method == 'get':
                return product.css(selector).get()
            elif method == 'getall':
                return product.css(selector).getall()
            elif method == 're_first':
                return product.css(selector).re_first(regex)

        return FlipkartItem(
            product_id=extract_data(FlipkartSelectors.PRODUCT_ID),
            product_name=extract_data(FlipkartSelectors.PRODUCT_NAME),
            brand=extract_data(FlipkartSelectors.BRAND),
            category=extract_data(FlipkartSelectors.CATEGORY, method='get', regex=None),
            price=extract_data(FlipkartSelectors.PRICE),
            original_price=extract_data(FlipkartSelectors.ORIGINAL_PRICE),
            discount=extract_data(FlipkartSelectors.DISCOUNT),
            description=extract_data(FlipkartSelectors.DESCRIPTION),
            product_images=extract_data(FlipkartSelectors.PRODUCT_IMAGES, method='getall'),
            product_rating=extract_data(FlipkartSelectors.PRODUCT_RATING),
            review_count=extract_data(FlipkartSelectors.REVIEW_COUNT),
            availability=extract_data(FlipkartSelectors.AVAILABILITY),
            sku=extract_data(FlipkartSelectors.SKU),
            shipping_info=extract_data(FlipkartSelectors.SHIPPING_INFO),
            size_color_options=extract_data(FlipkartSelectors.SIZE_COLOR_OPTIONS, method='getall'),
            product_url=extract_data(FlipkartSelectors.PRODUCT_URL),
            product_dimensions=extract_data(FlipkartSelectors.PRODUCT_DIMENSIONS, method='re_first', regex=r'Dimensions: (.*)'),
            weight=extract_data(FlipkartSelectors.WEIGHT, method='re_first', regex=r'Weight: (.*)'),
            material=extract_data(FlipkartSelectors.MATERIAL, method='re_first', regex=r'Material: (.*)'),
            customer_questions=extract_data(FlipkartSelectors.CUSTOMER_QUESTIONS, method='re_first', regex=r'Questions: (.*)'),
            seller_info=extract_data(FlipkartSelectors.SELLER_INFO),
            return_policy=extract_data(FlipkartSelectors.RETURN_POLICY),
            warranty=extract_data(FlipkartSelectors.WARRANTY, method='re_first', regex=r'Warranty: (.*)'),
        )

    def send_to_queue(self, item):
        try:
            self.rmq.publish_message(str(item))
        except Exception as e:
            self.logger.error(f"Error sending to queue: {e}")

    def close(self, reason):
        self.rmq.close_connection()
        super(FlipkartSpider, self).close(reason)
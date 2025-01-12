import logging

class LoggingExtension:
    def __init__(self, stats):
        self.stats = stats

    @classmethod
    def from_crawler(cls, crawler):
        ext = cls(crawler.stats)
        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        return ext

    def spider_opened(self, spider):
        logging.info(f"Spider {spider.name} opened")

    def spider_closed(self, spider, reason):
        logging.info(f"Spider {spider.name} closed: {reason}")

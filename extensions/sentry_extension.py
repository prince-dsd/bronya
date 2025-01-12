import sentry_sdk
from scrapy import signals

class SentryExtension:
    def __init__(self, dsn, client_options):
        sentry_sdk.init(dsn=dsn, **client_options)

    @classmethod
    def from_crawler(cls, crawler):
        dsn = crawler.settings.get('SENTRY_DSN')
        client_options = crawler.settings.get('SENTRY_CLIENT_OPTIONS', {})
        ext = cls(dsn, client_options)
        crawler.signals.connect(ext.spider_error, signal=signals.spider_error)
        return ext

    def spider_error(self, failure, response, spider):
        sentry_sdk.capture_exception(failure.value)

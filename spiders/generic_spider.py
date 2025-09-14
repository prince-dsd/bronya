import scrapy
import json
import yaml
import os
from scrapy.http import FormRequest

class GenericSpider(scrapy.Spider):
    name = "generic_spider"
    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'DOWNLOAD_DELAY': 2,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 2,
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    def __init__(self, config_path=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not config_path:
            raise ValueError("config_path argument is required")
        self.config = self.load_config(config_path)
        self.start_urls = self.config.get('start_urls', [])
        self.selectors = self.config.get('selectors', {})
        self.pagination = self.config.get('pagination', {})
        self.login = self.config.get('login', None)
        self.cookies = self.config.get('cookies', None)

    def load_config(self, path):
        ext = os.path.splitext(path)[1].lower()
        with open(path, 'r') as f:
            if ext in ['.yaml', '.yml']:
                return yaml.safe_load(f)
            elif ext == '.json':
                return json.load(f)
            else:
                raise ValueError("Unsupported config file format: {}".format(ext))

    def start_requests(self):
        if self.login:
            login_url = self.login.get('url')
            formdata = self.login.get('formdata', {})
            yield FormRequest(
                url=login_url,
                formdata=formdata,
                callback=self.after_login
            )
        else:
            for url in self.start_urls:
                yield scrapy.Request(url, cookies=self.cookies, callback=self.parse)

    def after_login(self, response):
        for url in self.start_urls:
            yield scrapy.Request(url, cookies=self.cookies, callback=self.parse)

    def parse(self, response):
        item = {}
        for key, selector in self.selectors.items():
            item[key] = response.css(selector).get(default='').strip()
        yield item

        # Pagination
        next_page_selector = self.pagination.get('next_page_selector')
        if next_page_selector:
            next_page = response.css(next_page_selector).get()
            if next_page:
                yield response.follow(next_page, self.parse)

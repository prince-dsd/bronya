import scrapy

class NewsItems(scrapy.Item):
    url = scrapy.Field() # String
    article_source = scrapy.Field() # String
    article_type = scrapy.Field() # String
    title = scrapy.Field() # String
    date_published = scrapy.Field() # String
    authors = scrapy.Field() # List 
    tags = scrapy.Field() # List
    content = scrapy.Field() # List
    content_html = scrapy.Field() # String
    article_images = scrapy.Field() # List
    article_videos = scrapy.Field() # List
    external_links = scrapy.Field() # List

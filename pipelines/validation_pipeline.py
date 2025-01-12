from scrapy.exceptions import DropItem

class ValidationPipeline:
    def process_item(self, item, spider):
        if not item.get('title') or not item.get('link'):
            raise DropItem("Missing title or link in %s" % item)
        return item

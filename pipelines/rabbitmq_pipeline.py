from rmq import RMQConnection

class RabbitMQPipeline:
    def __init__(self):
        self.rmq = RMQConnection(queue_name='news_queue')

    def process_item(self, item, spider):
        try:
            self.rmq.publish_message(str(item))
        except Exception as e:
            spider.logger.error(f"Error sending to queue: {e}")
        return item

    def close_spider(self, spider):
        self.rmq.close_connection()

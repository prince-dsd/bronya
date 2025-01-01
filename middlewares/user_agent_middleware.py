import random

class UserAgentMiddleware:
    def __init__(self, user_agents):
        self.user_agents = user_agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            user_agents=crawler.settings.get('USER_AGENTS')
        )

    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.user_agents)
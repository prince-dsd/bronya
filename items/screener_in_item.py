import scrapy

class ScreenerInItem(scrapy.Item):
    symbol = scrapy.Field()            # Company symbol/ticker
    company_name = scrapy.Field()      # Company name
    market_cap = scrapy.Field()        # Market capitalization
    current_price = scrapy.Field()     # Current stock price
    high_price = scrapy.Field()        # 52-week high price
    low_price = scrapy.Field()         # 52-week low price
    pe_ratio = scrapy.Field()          # Price to Earnings ratio
    book_value = scrapy.Field()        # Book value per share
    dividend_yield = scrapy.Field()    # Dividend yield
    roce = scrapy.Field()             # Return on Capital Employed
    roe = scrapy.Field()              # Return on Equity
    face_value = scrapy.Field()       # Face value per share
    sector = scrapy.Field()           # Industry sector
    profit_growth = scrapy.Field()    # Profit growth
    sales_growth = scrapy.Field()     # Sales growth
    promoter_holding = scrapy.Field() # Promoter holding percentage
    debt_to_equity = scrapy.Field()   # Debt to Equity ratio
    working_capital = scrapy.Field()  # Working capital

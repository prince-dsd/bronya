from sqlalchemy import Column, String, DECIMAL, TEXT, DateTime, Integer, Boolean
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.ext.declarative import declarative_base
from .mixins import (
    MysqlPrimaryKeyMixin,
    MysqlStatusMixin,
    MysqlTimestampsMixin,
    MysqlExceptionMixin,
    MysqlPriorityAttemptMixin,
    JSONSerializable,
)

Base = declarative_base()

class StockItemModel(
    Base,
    MysqlPrimaryKeyMixin,
    MysqlStatusMixin,
    MysqlTimestampsMixin,
    MysqlExceptionMixin,
    MysqlPriorityAttemptMixin,
    JSONSerializable,
):
    __tablename__ = 'stock_items'

    # Basic Stock Information
    symbol = Column(String(20), nullable=False, unique=True, index=True)
    company_name = Column(String(255), nullable=False)
    exchange = Column(String(50), nullable=False)
    sector = Column(String(100), nullable=True)
    industry = Column(String(100), nullable=True)

    # Price Information
    current_price = Column(DECIMAL(10, 2), nullable=True)
    open_price = Column(DECIMAL(10, 2), nullable=True)
    close_price = Column(DECIMAL(10, 2), nullable=True)
    high_price = Column(DECIMAL(10, 2), nullable=True)
    low_price = Column(DECIMAL(10, 2), nullable=True)
    previous_close = Column(DECIMAL(10, 2), nullable=True)

    # Volume Information
    volume = Column(MEDIUMINT(unsigned=True), nullable=True)
    average_volume = Column(MEDIUMINT(unsigned=True), nullable=True)

    # Market Data
    market_cap = Column(DECIMAL(20, 2), nullable=True)
    pe_ratio = Column(DECIMAL(10, 2), nullable=True)
    eps = Column(DECIMAL(10, 2), nullable=True)
    dividend_yield = Column(DECIMAL(5, 2), nullable=True)
    beta = Column(DECIMAL(5, 2), nullable=True)

    # Price Changes
    price_change = Column(DECIMAL(10, 2), nullable=True)
    price_change_percent = Column(DECIMAL(5, 2), nullable=True)
    year_high = Column(DECIMAL(10, 2), nullable=True)
    year_low = Column(DECIMAL(10, 2), nullable=True)

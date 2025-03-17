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

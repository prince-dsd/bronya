from sqlalchemy import Column, String, DECIMAL, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from .mixins import (
    MysqlPrimaryKeyMixin,
    MysqlStatusMixin,
    MysqlTimestampsMixin,
)

Base = declarative_base()

class ScreenerItemModel(Base, MysqlPrimaryKeyMixin, MysqlStatusMixin, MysqlTimestampsMixin):
    __tablename__ = 'screener_items'

    symbol = Column(String(10), nullable=False, index=True)
    company_name = Column(String(255), nullable=True)
    market_cap = Column(BigInteger, nullable=True)
    pe_ratio = Column(DECIMAL(10, 2), nullable=True)
    price = Column(DECIMAL(10, 2), nullable=True)
    volume = Column(BigInteger, nullable=True)
    sector = Column(String(100), nullable=True)
    industry = Column(String(100), nullable=True)
    dividend_yield = Column(DECIMAL(5, 2), nullable=True)
    eps = Column(DECIMAL(10, 2), nullable=True)
    beta = Column(DECIMAL(5, 2), nullable=True)
    high_52_week = Column(DECIMAL(10, 2), nullable=True)
    low_52_week = Column(DECIMAL(10, 2), nullable=True)
    moving_avg_50d = Column(DECIMAL(10, 2), nullable=True)
    moving_avg_200d = Column(DECIMAL(10, 2), nullable=True)
    relative_volume = Column(DECIMAL(10, 2), nullable=True)
    change_percent = Column(DECIMAL(5, 2), nullable=True)

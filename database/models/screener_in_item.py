from sqlalchemy import Column, String, DECIMAL, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from .mixins import (
    MysqlPrimaryKeyMixin,
    MysqlStatusMixin,
    MysqlTimestampsMixin,
)

Base = declarative_base()

class ScreenerInItemModel(Base, MysqlPrimaryKeyMixin, MysqlStatusMixin, MysqlTimestampsMixin):
    __tablename__ = 'screener_in_items'

    symbol = Column(String(20), nullable=False, index=True)
    company_name = Column(String(255), nullable=True)
    market_cap = Column(BigInteger, nullable=True)
    current_price = Column(DECIMAL(10, 2), nullable=True)
    high_price = Column(DECIMAL(10, 2), nullable=True)
    low_price = Column(DECIMAL(10, 2), nullable=True)
    pe_ratio = Column(DECIMAL(10, 2), nullable=True)
    book_value = Column(DECIMAL(10, 2), nullable=True)
    dividend_yield = Column(DECIMAL(5, 2), nullable=True)
    roce = Column(DECIMAL(5, 2), nullable=True)
    roe = Column(DECIMAL(5, 2), nullable=True)
    face_value = Column(DECIMAL(10, 2), nullable=True)
    sector = Column(String(100), nullable=True)
    profit_growth = Column(DECIMAL(5, 2), nullable=True)
    sales_growth = Column(DECIMAL(5, 2), nullable=True)
    promoter_holding = Column(DECIMAL(5, 2), nullable=True)
    debt_to_equity = Column(DECIMAL(5, 2), nullable=True)
    working_capital = Column(BigInteger, nullable=True)

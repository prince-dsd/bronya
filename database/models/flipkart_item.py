from sqlalchemy import Column, String, DECIMAL, TEXT
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.ext.declarative import declarative_base
from .mixins import (
    MysqlPrimaryKeyMixin,
    MysqlStatusMixin,
    MysqlTimestampsMixin,
    MysqlExceptionMixin,
    MysqlCoordinatesMixin,
    MysqlPriorityAttemptMixin,
    JSONSerializable,
)

Base = declarative_base()

class FlipkartItemModel(
    Base,
    MysqlPrimaryKeyMixin,
    MysqlStatusMixin,
    MysqlTimestampsMixin,
    MysqlExceptionMixin,
    MysqlCoordinatesMixin,
    MysqlPriorityAttemptMixin,
    JSONSerializable,
):
    __tablename__ = 'flipkart_items'

    product_id = Column(String(255), nullable=True, unique=False)
    product_name = Column(String(255), nullable=True, unique=False)
    brand = Column(String(255), nullable=True, unique=False)
    category = Column(String(255), nullable=True, unique=False)
    price = Column(DECIMAL(10, 2), nullable=True, unique=False)
    original_price = Column(DECIMAL(10, 2), nullable=True, unique=False)
    discount = Column(String(255), nullable=True, unique=False)
    description = Column(TEXT, nullable=True, unique=False)
    product_images = Column(TEXT, nullable=True, unique=False)
    product_rating = Column(DECIMAL(3, 2), nullable=True, unique=False)
    review_count = Column(MEDIUMINT(unsigned=True), nullable=True, unique=False)
    availability = Column(String(255), nullable=True, unique=False)
    sku = Column(String(255), nullable=True, unique=False)
    shipping_info = Column(TEXT, nullable=True, unique=False)
    size_color_options = Column(TEXT, nullable=True, unique=False)
    product_url = Column(String(255), nullable=True, unique=False)
    product_dimensions = Column(String(255), nullable=True, unique=False)
    weight = Column(DECIMAL(10, 2), nullable=True, unique=False)
    material = Column(String(255), nullable=True, unique=False)
    customer_questions = Column(TEXT, nullable=True, unique=False)
    seller_info = Column(TEXT, nullable=True, unique=False)
    return_policy = Column(TEXT, nullable=True, unique=False)
    warranty = Column(TEXT, nullable=True, unique=False)

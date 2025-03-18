from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class StockItems(BaseModel):
    # Basic Stock Information
    symbol: Optional[str]
    company_name: Optional[str]
    exchange: Optional[str]
    sector: Optional[str]
    industry: Optional[str]

    # Price Information
    current_price: Optional[Decimal]
    open_price: Optional[Decimal]
    close_price: Optional[Decimal]
    high_price: Optional[Decimal]
    low_price: Optional[Decimal]
    previous_close: Optional[Decimal]

    # Volume Information
    volume: Optional[int]
    average_volume: Optional[int]

    # Market Data
    market_cap: Optional[Decimal]
    pe_ratio: Optional[Decimal]
    eps: Optional[Decimal]
    dividend_yield: Optional[Decimal]
    beta: Optional[Decimal]

    # Price Changes
    price_change: Optional[Decimal]
    price_change_percent: Optional[Decimal]
    year_high: Optional[Decimal]
    year_low: Optional[Decimal]

    # Additional Information
    description: Optional[str]
    website: Optional[str]
    is_active: Optional[bool] = True

    # Financial Metrics
    revenue: Optional[Decimal]
    profit_margin: Optional[Decimal]
    debt_to_equity: Optional[Decimal]
    free_cash_flow: Optional[Decimal]

    # Trading Information
    trading_currency: Optional[str]
    lot_size: Optional[int]
    face_value: Optional[Decimal]
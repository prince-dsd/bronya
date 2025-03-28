from pydantic import BaseModel
from typing import Optional

class ScreenerInItem(BaseModel):
    symbol: str
    company_name: Optional[str]
    market_cap: Optional[str]
    current_price: Optional[str]
    high_price: Optional[str]
    low_price: Optional[str]
    pe_ratio: Optional[str]
    book_value: Optional[str]
    dividend_yield: Optional[str]
    roce: Optional[str]
    roe: Optional[str]
    face_value: Optional[str]
    sector: Optional[str]
    profit_growth: Optional[str]
    sales_growth: Optional[str]
    promoter_holding: Optional[str]
    debt_to_equity: Optional[str]
    working_capital: Optional[str]

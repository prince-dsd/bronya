from pydantic import BaseModel
from typing import Optional

class ScreenerItem(BaseModel):
    symbol: str
    company_name: Optional[str]
    market_cap: Optional[str]
    pe_ratio: Optional[str]
    price: Optional[str]
    volume: Optional[str]
    sector: Optional[str]
    industry: Optional[str]
    dividend_yield: Optional[str]
    eps: Optional[str]
    beta: Optional[str]
    high_52_week: Optional[str]
    low_52_week: Optional[str]
    moving_avg_50d: Optional[str]
    moving_avg_200d: Optional[str]
    relative_volume: Optional[str]
    change_percent: Optional[str]

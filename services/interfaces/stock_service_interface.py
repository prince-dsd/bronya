from abc import ABC, abstractmethod
from typing import Any
from items.stock_items import StockItems

class StockServiceInterface(ABC):
    @abstractmethod
    def extract_stock_data(self, response: Any, symbol: str) -> StockItems:
        pass

    @abstractmethod
    def send_to_queue(self, item: StockItems) -> None:
        pass

    @abstractmethod
    def close_connection(self) -> None:
        pass
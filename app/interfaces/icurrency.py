from abc import ABC, abstractmethod
from typing import Optional
from app.models.currency_model import Currency


class ICurrencyService(ABC):

    @abstractmethod
    def _convert_date_format(self, date_str: Optional[str]) -> str:
        pass

    @abstractmethod
    def get_currency(self, currency: Optional[str] = None, date: Optional[str] = None) -> Currency:
        pass

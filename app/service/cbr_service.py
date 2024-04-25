from datetime import datetime
from fastapi import HTTPException
from typing import Optional
import requests
from xml.etree import ElementTree as ET
from app.models.currency_model import Currency
from app.interfaces.icurrency import ICurrencyService


class CbrCurrencyService(ICurrencyService):

    def _convert_date_format(self, date_str: Optional[str]) -> str:
        if date_str is None:
            return datetime.now().strftime("%d/%m/%Y")
        try:
            valid_date = datetime.strptime(date_str, "%Y-%m-%d")
            return valid_date.strftime("%d/%m/%Y")
        except ValueError:
            raise HTTPException(status_code=400, detail="Date format must be YYYY-MM-DD")

    def get_currency(self, currency: Optional[str] = None, date: Optional[str] = None) -> Currency:
        date_str = self._convert_date_format(date)
        url = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={date_str}"
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            raise HTTPException(status_code=500, detail=str(e))

        tree = ET.fromstring(response.content)
        currency_data = {}
        found_currency = False

        for valute in tree.findall("Valute"):
            char_code = valute.find("CharCode").text
            value = valute.find("Value").text.replace(",", ".")
            if currency is None or currency.upper() == char_code:
                currency_data[char_code] = float(value)
                if currency and currency.upper() == char_code:
                    found_currency = True
                    break

        if currency and not found_currency:
            raise HTTPException(status_code=404, detail=f"Currency {currency} not found.")

        return Currency(data=currency_data)

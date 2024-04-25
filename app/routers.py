from typing import Optional
from fastapi import APIRouter
from app.models.currency_model import Currency
from app.models.info_model import Info
from app.service.info_service import InfoService
from app.service.cbr_service import CbrCurrencyService
from .swagger_responses import info_responses, currency_responses

router = APIRouter()

currency_service = CbrCurrencyService()  # Instantiate your concrete implementation


@router.get("/info", response_model=Info, responses=info_responses)
async def info() -> Info:
    return InfoService().get_info()


@router.get("/info/currency", response_model=Currency, responses=currency_responses)
async def info_currency(currency: Optional[str] = None, date: Optional[str] = None) -> Currency:
    currency_service = CbrCurrencyService()
    return currency_service.get_currency(currency, date)

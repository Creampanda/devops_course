from pydantic import BaseModel


class Currency(BaseModel):
    service: str = "currency"
    data: dict[str, float]

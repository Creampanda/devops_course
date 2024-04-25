from pydantic import BaseModel


class Info(BaseModel):
    version: str
    service: str
    author: str

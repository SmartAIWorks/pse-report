from pydantic import BaseModel

class Stock(BaseModel):
    name: str
    code: str
    price: float
    currency: str
    percent_change:float
    volume: int

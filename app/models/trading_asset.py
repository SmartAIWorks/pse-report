from pydantic import BaseModel

class TradingAsset(BaseModel):
    name: str
    code: str
    price: float
    currency: str
    percent_change:float
    volume: int
    value: int
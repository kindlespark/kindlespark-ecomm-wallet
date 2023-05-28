from pydantic import BaseModel


class Wallet(BaseModel):
    id: int
    brand: str
    colour: str
    price: float

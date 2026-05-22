from pydantic import BaseModel

class PaymentCreate(BaseModel):
    parent_name: str
    amount: int
    comment: str



   

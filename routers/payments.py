from fastapi import APIRouter
from database.session import Sessionlocal
from models.payment_model import Payment

router = APIRouter()

@router.post("/payments")
def create_payment():
    db = Sessionlocal()

    payment = Payment(
        parent_name = "Роман Романовчи",
        amount = 1000, 
        status = "pending"
    )

    db.add(payment)
    db.commit()
    db.refresh(payment) # обновляет обьект свежими данными из БД

    return payment



from fastapi import APIRouter, Request
from database.session import Sessionlocal
from models.payment_model import Payment
from schemas.payment_schemas import PaymentCreate
from services.payment_service import create_payment_in_yoocassa
from schemas.yookassa_schemas import WebhookData
router = APIRouter()

@router.post("/create_payment")
def create_payment(payment: PaymentCreate):
    db = Sessionlocal()

    try:
        new_payment = Payment(
            parent_name=payment.parent_name,
            amount=payment.amount,
            comment=payment.comment
        )
        
        db.add(new_payment)
        db.commit()
        db.refresh(new_payment)

    

        yookassa_payment = create_payment_in_yoocassa(payment.amount, payment.comment)

        new_payment.yoocassa_payment_id = yookassa_payment.id #сохраняем payment_id

        db.commit()
        db.refresh(new_payment)

        return {
            "payment_id": new_payment.id,
            "yookassa_payment_id": yookassa_payment.id,
            "confirmation_url": yookassa_payment.confirmation.confirmation_url
        }
    
    finally:
        db.close()


@router.post("/webhook")
async def webhook(data: WebhookData):

    event = data.event
    payment_id = data.object.id

    db = Sessionlocal()

    try:
        payment = db.query(Payment).filter(Payment.yoocassa_payment_id == payment_id).first()

        if not payment:
            return {"message": "Payment not found"}
        
        if event == "payment.succeeded":
            payment.status = "succeeded"
        
        elif event == "payment.canceled":
            payment.status = "canceled"
        
        db.commit()

        return {"message": "Webhook received"}
    
    finally:
        db.close()




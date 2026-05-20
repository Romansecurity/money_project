from fastapi import APIRouter, HTTPException
from database.session import Sessionlocal
from models.payment_model import Payment
from schemas.payment_schemas import PaymentCreate

router = APIRouter()

@router.post("/payments")
def create_payment(payment: PaymentCreate):
    db = Sessionlocal()
    try:

        new_payment = Payment(
            parent_name=payment.parent_name,
            amount=payment.amount
        )

        db.add(new_payment)
        db.commit()
        db.refresh(new_payment)

        return new_payment
    
    finally:
        db.close()

@router.get("/payments")
def get_payments():
    db = Sessionlocal()
    try:
        payments = db.query(Payment).all()

        return payments
    
    finally:
        db.close()


@router.get("/payments/{id}")
def get_id(id: int):
    db = Sessionlocal()
    try:
        payment = db.query(Payment).filter(Payment.id == id).first() #first- +выполнить запрос

        if payment is None:
            raise HTTPException(status_code=404, detail="Payment not found")
    
        return payment
    
    finally:
        db.close()

@router.put("/payments/{id}")
def update_payment(id: int, payment: PaymentCreate):
    db = Sessionlocal()
    try:
        db_payment = db.query(Payment).filter(Payment.id == id).first()
        if db_payment is None:
            raise HTTPException(status_code=404, detail="Payment not found")
        
        db_payment.parent_name = payment.parent_name
        db_payment.amount = payment.amount

        db.commit()
        db.refresh(db_payment)
        return db_payment
    
    finally:
        db.close()

@router.delete("/payments/{id}")
def delete_payment(id: int):
    db = Sessionlocal()
    try:
        payment = db.query(Payment).filter(Payment.id == id).first()
        if payment is None:
            raise HTTPException(status_code=404, detail="Payment not found")
        
        db.delete(payment)
        db.commit()
        return {"detail": "Payment deleted successfully"}
    
    finally:
        db.close()
    
@router.delete("/payments")
def delete_all():
    db = Sessionlocal()
    try:
        db.query(Payment).delete()
        db.commit()
        return {"detail": "All payments deleted successfully"}
    
    finally:
        db.close()
from yookassa import Payment # класс для работы с API Yookassa
from yookassa import Configuration
import os

Configuration.account_id = os.getenv("YOOKASSA_SHOP_KEY")
Configuration.secret_key = os.getenv("YOOKASSA_SECRET_KEY")

def create_payment_in_yoocassa(amount, comment):
    payment = Payment.create({
        "amount": {
            "value": str(amount),
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://magenta-sable-b50a0b.netlify.app/"
        },
        "capture": True,
        "description": comment
    })

    return payment


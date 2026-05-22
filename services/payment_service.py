from yookassa import Payment # класс для работы с API Yookassa

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


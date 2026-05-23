# Money Project — YooKassa Payment System

Production-ready payment system built with FastAPI + YooKassa + PostgreSQL, deployed on Render (backend + DB) and Netlify (frontend).

🌐 **Frontend:** https://magenta-sable-b50a0b.netlify.app/  
⚙️ **Backend API:** https://money-project-6.onrender.com

---

## Tech Stack

**Backend:** Python 3.11, FastAPI, Uvicorn, SQLAlchemy, Psycopg2, YooKassa SDK  
**Database:** PostgreSQL (Render Managed)  
**Frontend:** HTML, Vanilla JavaScript  
**Deployment:** Render (API + DB), Netlify (Frontend)

---

## How It Works

1. User clicks **Pay** on the frontend
2. Frontend sends `POST /create_payment` to the backend
3. Backend creates a payment via YooKassa API
4. YooKassa returns a `confirmation_url`
5. User gets redirected to the YooKassa checkout page

---

## API

### `POST /create_payment`

**Request:**
```json
{
  "amount": 100,
  "comment": "Order payment"
}
```

**Response:**
```json
{
  "payment_url": "https://yoomoney.ru/checkout/..."
}
```

---

## Environment Variables

```
DATABASE_URL=postgresql+psycopg2://USER:PASSWORD@HOST:5432/DBNAME
YOOKASSA_SHOP_ID=your_shop_id
YOOKASSA_SECRET_KEY=your_secret_key
```

---

## Database

Table `payments`:

| Column | Type |
|--------|------|
| id | Integer (PK) |
| amount | Integer |
| status | String |
| comment | Text |
| created_at | DateTime |

---

## Project Structure

```
money_project/
├── main.py
├── requirements.txt
├── database/session.py
├── models/payment_model.py
├── schemas/
│   ├── payment_schemas.py
│   └── yookassa_schemas.py
├── routers/payments.py
├── services/payment_service.py
└── fronted/index-2.html
```

---

## Deployment (Render)

**Build command:**
```
pip install -r requirements.txt
```

**Start command:**
```
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Required env vars: `DATABASE_URL`, `YOOKASSA_SHOP_ID`, `YOOKASSA_SECRET_KEY`

> Note: Render free tier may have cold start delays.

---

## Roadmap

- [ ] YooKassa webhooks (payment status tracking)
- [ ] Admin dashboard
- [ ] JWT authentication
- [ ] Docker deployment
- [ ] CI/CD via GitHub → Render auto deploy

---

## Author

**RomanSecurity** — backend project for learning payment systems, deployment, and API integration.

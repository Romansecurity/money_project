from fastapi import FastAPI
from routers.payments import router as payments_router 

app = FastAPI()
app.include_router(payments_router)
import services.config
from fastapi import FastAPI
from database.session import engine, Base
from routers.payments import router as payments_router 



app = FastAPI()
app.include_router(payments_router)


Base.metadata.create_all(bind=engine)


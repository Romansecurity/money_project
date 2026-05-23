from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.session import engine, Base
from routers.payments import router as payments_router 


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(payments_router)


@app.on_event("startup")
def startup():
    # безопасно создаёт таблицы
    Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Server is running!"}
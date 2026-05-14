from database.session import engine, Base
from models.payment_model import Payment #нужен для регистрации модели в БД 
#Base.metadata  - хранилище информации обо всех таблицах
#create_all - метод для создания всех таблиц

Base.metadata.create_all(bind=engine)
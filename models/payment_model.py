from sqlalchemy import Column, Integer, String, DateTime
#Column - класс для создания колонок в таблице
from database.session import Base
from sqlalchemy.sql import func #импорт пространства имен для работы с функ. SQL

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    parent_name = Column(String)
    amount = Column(Integer)
    status = Column(String, default="pending") #незавершенный платеж
    date_time = Column(DateTime(timezone=True), server_default=func.now()) #возвращает текущее время 
    yoocassa_payment_id = Column(String)
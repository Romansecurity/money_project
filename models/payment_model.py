from sqlalchemy import Column, Integer, String, DateTime, Text
from database.session import Base
from sqlalchemy.sql import func 

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    parent_name = Column(String)
    amount = Column(Integer)
    comment = Column(Text)
    status = Column(String, default="pending") #незавершенный платеж
    date_time = Column(DateTime(timezone=True), server_default=func.now()) #возвращает текущее время 
    yoocassa_payment_id = Column(String)
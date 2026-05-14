from sqlalchemy import create_engine #движок, отвечающий за соединение с БД
from sqlalchemy.orm import declarative_base #клдасс для создания всех ORM моделей
from sqlalchemy.orm import sessionmaker #класс для создания сессий, которые будут работать с БД (INSERT, UPDATE и тд)

DATA_BASE = "postgresql://roman@localhost/payments_db"

engine = create_engine(DATA_BASE)

Sessionlocal = sessionmaker(bind=engine)

Base = declarative_base()
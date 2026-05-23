from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 
import os
from dotenv import load_dotenv

load_dotenv()
DATA_BASE = os.getenv("DATA_BASE")

engine = create_engine(DATA_BASE)

Sessionlocal = sessionmaker(bind=engine)

Base = declarative_base()
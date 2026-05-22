from yookassa import Configuration
import os
from dotenv import load_dotenv

load_dotenv()

Configuration.account_id = os.getenv("SHOP_ID")
Configuration.secret_key = os.getenv("SECRET_ID")


print("yookassa configuration loaded successfully")
print(f"SHOP_ID: {Configuration.account_id}")
print(f"SECRET_ID: {Configuration.secret_key}")

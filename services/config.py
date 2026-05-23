from yookassa import Configuration
import os

Configuration.account_id = os.getenv("YOOKASSA_SHOP_KEY")
Configuration.secret_key = os.getenv("YOOKASSA_SECRET_KEY")


print("yookassa configuration loaded successfully")
print(f"SHOP_ID: {Configuration.account_id}")
print(f"SECRET_ID: {Configuration.secret_key}")

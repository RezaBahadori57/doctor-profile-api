from pymongo import MongoClient
import os

# MongoDB connection URI (در حالت عادی روی لوکال MongoDB اجرا میشه)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# اتصال به کلاینت MongoDB
client = MongoClient(MONGO_URI)

# انتخاب دیتابیس (میتونی اسمشو تغییر بدی)
db = client["doctor_appointment_db"]

def get_db():
    return db

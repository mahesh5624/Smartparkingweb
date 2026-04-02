from flask import Flask, jsonify, request, redirect, send_from_directory
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# 🔗 MongoDB connection (FINAL WORKING)
MONGO_URL = "mongodb+srv://admin:admin123@cluster0.vjwxtdc.mongodb.net/?retryWrites=true&w=majority"

try:
    client = MongoClient(MONGO_URL)
    db = client["parking"]
    collection = db["logs"]
    print("✅ MongoDB Connected")
except Exception as e:
    print("❌ MongoDB Error:", e)
    collection = None

# 🔐 Login
USERNAME = "admin"
PASSWORD = "1234"

# 🅿️ Slot data
slots = [False, True, False, True, False, False]

# ================= ROUTES =================

@app.route("/")
def home():
    return send_from_directory('.', 'login.html')


@app.route("/login", methods=["POST"])
def login():
    user = request.form.get("username")
    pwd = request.form.get("password")

    if user == USERNAME and pwd == PASSWORD:
        return redirect("/dashboard")
    return "Login Failed"


@app.route("/dashboard")
def dashboard():
    return send_from_directory('.', 'index.html')


# 📊 Get slot status
@app.route("/api/slots")
def get_slots():
    return jsonify({
        "slots": slots,
        "occupied": sum(slots),
        "total": len(slots)
    })


# 💾 Store data in MongoDB
@app.route("/api/store", methods=["POST"])
def store_data():
    if collection is None:
        return {"message": "DB not connected"}

    data = request.json

    record = {
        "plate": data.get("plate"),
        "slot": data.get("slot"),
        "status": data.get("status"),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    collection.insert_one(record)

    return {"message": "Data Stored Successfully"}


# 📋 Get logs
@app.route("/api/logs")
def get_logs():
    if collection is None:
        return jsonify([])

    logs = list(collection.find({}, {"_id": 0}))
    return jsonify(logs)


# ================= RUN =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

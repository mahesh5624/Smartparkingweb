from flask import Flask, jsonify, request, redirect, send_from_directory
from pymongo import MongoClient
from datetime import datetime
import requests

app = Flask(__name__)

# 🔗 MongoDB
MONGO_URL = "mongodb+srv://admin:admin123@cluster0.vjwxtdc.mongodb.net/?retryWrites=true&w=majority"

try:
    client = MongoClient(MONGO_URL)
    db = client["parking"]
    collection = db["logs"]
    print("MongoDB Connected")
except Exception as e:
    print("MongoDB Error:", e)
    collection = None

# 🔐 Login
USERNAME = "admin"
PASSWORD = "1234"

# 🌐 ESP32 URL (change if needed)
ESP32_URL = "http://192.168.4.1"

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


# 📊 REAL SLOT DATA FROM ESP32
@app.route("/api/slots")
def get_slots():
    try:
        res = requests.get(f"{ESP32_URL}/get_slots", timeout=3)
        data = res.json()

        return jsonify({
            "slots": data["slots"],
            "occupied": sum(data["slots"]),
            "total": len(data["slots"])
        })
    except:
        return jsonify({
            "slots": [False]*6,
            "occupied": 0,
            "total": 6
        })


# 💾 STORE DATA FROM OCR
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

    return {"message": "Stored"}


# 📋 GET LOGS
@app.route("/api/logs")
def get_logs():
    if collection is None:
        return jsonify([])

    logs = list(collection.find({}, {"_id": 0}))
    return jsonify(logs)


# 🚀 RUN
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

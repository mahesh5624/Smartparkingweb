from flask import Flask, jsonify, request, redirect, send_from_directory
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# 🔗 MongoDB Atlas connection
client = MongoClient("mongodb+srv://admin:admin123@cluster0.vjwxtdc.mongodb.net/")
db = client["parking"]
collection = db["logs"]

# 🔐 Login credentials
USERNAME = "admin"
PASSWORD = "1234"

# 🅿️ Slot status (False = Free, True = Occupied)
slots = [False, True, False, True, False, False]

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

# 📊 Get slots
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
    data = request.json

    record = {
        "plate": data.get("plate"),
        "slot": data.get("slot"),
        "status": data.get("status"),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    collection.insert_one(record)

    return {"message": "stored"}

# 📋 Get logs
@app.route("/api/logs")
def get_logs():
    logs = list(collection.find({}, {"_id": 0}))
    return jsonify(logs)

if __name__ == "__main__":
    app.run()

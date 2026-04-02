from flask import Flask, jsonify, send_from_directory
import random

app = Flask(__name__)

# Dummy slot data (simulate real system)
slots = [False, True, False, True, False, False]  
# False = Free, True = Occupied

@app.route("/api/slots")
def get_slots():
    # simulate changing slots
    global slots
    slots = [random.choice([True, False]) for _ in range(6)]
    
    return jsonify({
        "slots": slots,
        "occupied": sum(slots),
        "total": len(slots)
    })

@app.route("/")
def home():
    return send_from_directory('.', 'index.html')

if __name__ == "__main__":
    app.run()
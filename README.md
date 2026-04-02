# 🚗 Smart Parking Management System

A real-time smart parking system that integrates **YOLOv8 vehicle detection**, **OCR-based number plate recognition**, **ESP32 IoT hardware**, and a **web dashboard with MongoDB** for monitoring and management.

---

## 🌐 Live Website

👉 https://smartparkingweb-bs81.onrender.com

---

## 🧠 System Architecture

```
Camera → YOLOv8 + OCR → Flask API → MongoDB → Web Dashboard
                         ↓
                     ESP32 (Gate + Slots)
```

---

## ✨ Features

### 🔍 AI & Detection

* YOLOv8 real-time vehicle detection
* PaddleOCR for number plate recognition
* Supports cars, bikes, trucks, buses

### 🌐 Web Dashboard

* Admin login system
* Real-time parking slot status
* Vehicle entry logs (plate, slot, time)
* Responsive UI

### 🗄️ Database

* MongoDB Atlas (cloud database)
* Stores:

  * Plate number
  * Slot number
  * Status (occupied/free)
  * Timestamp

### 📡 IoT Integration

* ESP32 microcontroller
* Gate automation (servo motor)
* Slot detection using sensors
* Real-time slot updates

---

## 🏗️ Project Structure

```
📁 SmartParkingWeb (Render)
 ├── app.py
 ├── index.html
 ├── login.html
 ├── requirements.txt

📁 OCR System (Local)
 ├── ocr.py

📁 ESP32
 ├── esp32.py
```

---

## 🚀 How It Works

### Entry Process

1. Camera captures vehicle
2. YOLO detects vehicle
3. OCR reads number plate
4. Data sent to Flask API
5. MongoDB stores entry
6. ESP32 opens gate
7. Slot assigned and updated

### Exit Process

1. Vehicle detected at exit
2. Slot released
3. Exit time updated in database

---

## 🔧 Technologies Used

* Python
* Flask
* MongoDB Atlas
* YOLOv8 (Ultralytics)
* PaddleOCR
* OpenCV
* ESP32 (IoT)
* HTML, CSS, JavaScript

---

## ⚠️ Important Note

* OCR + YOLO runs on **local system**
* Website runs on **Render (cloud)**
* ESP32 works on **local network**

---

## 💬 Interview Explanation

> "I developed a full-stack smart parking system integrating computer vision (YOLOv8), OCR, IoT hardware (ESP32), and a cloud-based web dashboard with MongoDB for real-time monitoring."

---

## 📌 Future Improvements

* Mobile app integration
* Slot reservation system
* Payment gateway
* AI-based parking prediction
* Multi-location support

---

## 👨‍💻 Author

Mahesh

---

🚗 Making Parking Smart and Efficient 🚗

# Multiple-Face-Recognition-Attendance-System-Using-Python

This project implements a **Multiple Face Recognition Attendance System** using the **Haar Cascade Classifier** for face detection and the **LBPH (Local Binary Patterns Histogram)** algorithm for face recognition. The system captures real-time video from a webcam, detects faces in each frame, identifies registered individuals, and automatically marks their attendance with **name, date, and timestamp** in a CSV file.

It is lightweight, fast, easy to train, and suitable for **schools, colleges, offices, and event check-ins**.

## ⭐ Key Features

* **Real-time multi-face detection** using Haar Cascade
* **LBPH-based face recognition** for accuracy and speed
* **Automatic attendance marking** with time and date
* **CSV-based attendance logs** for easy tracking
* **Simple dataset structure** — add images and retrain
* **Works on low-end hardware** (no GPU required)
* **Supports webcam or video file input**
* **Fully customizable thresholds and parameters**

---

## 📁 Project Structure

```
dataset/                # Training images (one folder per person)
trainer.yml             # LBPH trained model file
haarcascade_frontalface_default.xml  # Haar Cascade model
train_model.py          # Script to train LBPH recognizer
recognize.py            # Script for real-time recognition
attendance.csv          # Auto-generated attendance file
requirements.txt
README.md
```

---

## 🧠 How It Works

### 1️⃣ Face Detection

The system uses **Haar Cascade** to detect faces in every frame. It is a classical machine learning method known for being fast and lightweight.

### 2️⃣ Face Recognition

For each detected face, the system uses the **LBPH algorithm**, which converts the face region into a set of local binary patterns and compares them with trained data to identify the person.

### 3️⃣ Attendance Marking

Once a face is recognized:

* The system checks if the person’s name is already recorded for the day
* If not, it logs the **Name, Date, and Time** in `attendance.csv`

### 4️⃣ Real-Time Processing

The entire flow runs continuously via webcam or video input, allowing **multiple faces** to be recognized simultaneously.


Technologies Used

* **Python**
* **OpenCV**
* **Haar Cascade** (Face Detection)
* **LBPH Face Recognizer**
* **NumPy, Pandas**


Just tell me!


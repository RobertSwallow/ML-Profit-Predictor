# ML-Profit-Predictor

## 📊 Overview
**ML-Profit-Predictor** is a machine learning web application that forecasts a startup’s potential **profit** and **ROI** based on spending inputs and location.  
Built with **Python**, **scikit-learn**, and **Streamlit**, the app helps investors make more data-driven decisions. You can run it locally or inside a **Docker** container.

---

## 🚀 Features
- Enter values for:
  - **R&D Spend**
  - **Administration Spend**
  - **Marketing Spend**
  - **State** (optional)
- Predicts expected **Profit**
- Calculates **Return on Investment (ROI)**
- Flags whether ROI meets a **20% benchmark**
- Validates user inputs for reliability

---

## 📁 Files Included
- `app.py` — Streamlit web app  
- `model_with_states.pkl` — Trained Random Forest model  
- `requirements.txt` — Python dependencies  
- `Dockerfile` — For Docker-based deployment  
- `README.md` — This file

---

### 🔹 Run Locally (Without Docker)
1. Install Python 3.8 or later  
2. Install dependencies:

## 🛠️ Requirements

```bash
pip install -r requirements.txt

### Run the app
```bash
streamlit run app.py

### Open browser to
http://localhost:8501


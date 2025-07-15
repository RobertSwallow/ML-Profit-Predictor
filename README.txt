# Startup Profit Predictor

## Overview
This project is a **Startup Profit Predictor** built using Python, scikit-learn Random Forest regression, and Streamlit for a simple web UI. The model predicts profit based on R&D Spend, Administration Spend, Marketing Spend, and State. The app is containerized with Docker for easy deployment.

---

## Features
- Input fields for R&D Spend, Administration Spend, Marketing Spend, and select State
- Input validation for reasonable prediction ranges
- Predicts expected profit and calculates ROI based on user inputs
- Uses a trained Random Forest model saved as `model_with_states.pkl`
- Runs as an interactive web app via Streamlit

---

## Requirements
- Docker

---

## Files Included
- app.py
- model_with_states.pkl
- Dockerfile
- requirements.txt

---

## How to Run with Docker
1. run from directory containing Dockerfile:
	docker build -t capstone_app .
2. run the container
	docker run -p 8501:8501 capstone_app

## Final Notes
- The model expects Administration's spending to be above $50,000
- The model expects all spending to be below $400,000
- The model shows the amount of profit expected, given the input with a 
- Predicted ROI is calculated and shows if it is below or above 20%
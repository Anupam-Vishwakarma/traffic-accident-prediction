from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
import logging
from pathlib import Path

# ================================
# ✅ Setup Logging
# ================================
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ================================
# ✅ Define File Paths
# ================================
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "accident_severity_model.pkl"
ENCODERS_PATH = BASE_DIR / "models" / "label_encoders.pkl"
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"

# ================================
# ✅ Load Model, Encoders & Scaler
# ================================
try:
    model = joblib.load(MODEL_PATH)
    label_encoders = joblib.load(ENCODERS_PATH)
    scaler = joblib.load(SCALER_PATH)
    logger.info("✅ Model, encoders, and scaler loaded successfully.")
except Exception as e:
    logger.error(f"❌ Error loading model or preprocessors: {e}")
    raise e

# ================================
# ✅ Initialize FastAPI App
# ================================
app = FastAPI(
    title="🚦 Real-Time Traffic Congestion & Accident Prediction API",
    description="Predicts congestion severity and accident risk using trained ML model.",
    version="1.0.0"
)

# ================================
# ✅ Serve Frontend Files
# ================================
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/ui")
def ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# ================================
# ✅ Define Input Schema
# ================================
class TrafficInput(BaseModel):
    Start_Lat: float
    Start_Lng: float
    Distance_mi: float
    City: str
    State: str
    Temperature_F: float
    Humidity: float
    Pressure: float
    Visibility: float
    Wind_Speed: float
    Weather_Condition: str
    Sunrise_Sunset: str
    Traffic_Signal: int
    Hour: int
    Month: int
    Year: int

# ================================
# ✅ Home Route
# ================================
@app.get("/")
def home():
    return {
        "message": "Welcome to the Real-Time Traffic Prediction API 🚗",
        "usage": "Send a POST request to /predict with input data."
    }

# ================================
# ✅ Prediction Route
# ================================
@app.post("/predict")
def predict(data: TrafficInput):
    try:
        # Convert input data to DataFrame
        features = pd.DataFrame([{
            'Start_Lat': data.Start_Lat,
            'Start_Lng': data.Start_Lng,
            'Distance(mi)': data.Distance_mi,
            'City': data.City,
            'State': data.State,
            'Temperature(F)': data.Temperature_F,
            'Humidity(%)': data.Humidity,
            'Pressure(in)': data.Pressure,
            'Visibility(mi)': data.Visibility,
            'Wind_Speed(mph)': data.Wind_Speed,
            'Weather_Condition': data.Weather_Condition,
            'Sunrise_Sunset': data.Sunrise_Sunset,
            'Traffic_Signal': data.Traffic_Signal,
            'Hour': data.Hour,
            'Month': data.Month,
            'Year': data.Year
        }])

        # ======================
        # 1️⃣ Encode Categorical Columns
        # ======================
        cat_cols = ['City', 'State', 'Weather_Condition', 'Sunrise_Sunset']
        for col in cat_cols:
            if col in label_encoders:
                le = label_encoders[col]
                features[col] = features[col].apply(
                    lambda x: le.transform([x])[0] if x in le.classes_ else -1
                )

        # ======================
        # 2️⃣ Scale Numerical Columns
        # ======================
        num_cols = ['Start_Lat', 'Start_Lng', 'Distance(mi)', 'Temperature(F)',
                    'Humidity(%)', 'Pressure(in)', 'Visibility(mi)',
                    'Wind_Speed(mph)', 'Hour', 'Month', 'Year']

        features[num_cols] = scaler.transform(features[num_cols])

        # ======================
        # 3️⃣ Make Prediction
        # ======================
        prediction = int(model.predict(features)[0])

        # ======================
        # 4️⃣ Map Predicted Label
        # ======================
        labels = {
            0: "Low Congestion",
            1: "Moderate Congestion",
            2: "High Congestion",
            3: "Accident Prone"
        }
        result_label = labels.get(prediction, "Unknown")

        logger.info(f"✅ Prediction successful: {result_label}")

        return {
            "prediction_code": prediction,
            "category": result_label,
            "status": "success"
        }

    except Exception as e:
        logger.error(f"❌ Prediction error: {e}")
        return {"error": str(e), "status": "failed"}

# ================================
# ✅ Run Command
# ================================
# uvicorn main:app --reload

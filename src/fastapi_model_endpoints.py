import pandas as pd
import joblib
from fastapi import FastAPI, HTTPException


def load_model(filename):
    model = joblib.load(filename)
    print(f"Model loaded from {filename}")
    return model

def predict_with_model(model, data):
    try:
        df = pd.DataFrame([data])
        result = model.predict(df)
        return {
            # "prediction": result[0].item()
            "prediction": get_prediction_labels(result)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 

def get_prediction_labels(result):
    return "Failure" if result[0] == 1 else "No Failure"


model = load_model('models/rf_model.pkl')
app = FastAPI(title="Machine Failure Prediction API")

@app.get("/")
def home():
    return {"message": "Welcome to the Machine Failure Prediction API!"}

@app.post("/predict")
def predict(data: dict):
    print("Received data for prediction:", data)
    return predict_with_model(model, data)


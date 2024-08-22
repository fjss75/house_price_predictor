from fastapi import FastAPI
from typing import List
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load('model.joblib')

@app.post('/prediction')
def prediction(data: List[float]):
    columns = ['longitude','latitude','housing_median_age','total_rooms', 
               'total_bedrooms', 'population', 'households', 'median_income', 
               '<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN']
    
    features = pd.DataFrame([data], columns=columns)
    prediction = model.predict(features)[0]

    return{'price': round(prediction, 2)}

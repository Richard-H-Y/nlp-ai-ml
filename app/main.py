import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
model = joblib.load("model.joblib")

class Flower(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict(f: Flower):
    pred = model.predict([[f.sepal_length, f.sepal_width,
                           f.petal_length, f.petal_width]])
    return {"class": int(pred[0])}
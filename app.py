from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import os
from starlette.responses import RedirectResponse

from fastapi.responses import Response
from titanicSurvival.components.prediction import PredictionPipeline
import json
import pandas as pd

app = FastAPI()
class InputData(BaseModel):
    PassengerId: int
    Pclass: int
    Name: str
    Sex: str
    Age: int
    SibSp: int
    Parch: int
    Ticket: str
    Fare: float
    Cabin: str
    Embarked: str

@app.get("/",tags = ['authentication'])
async def index():
    return RedirectResponse(url='/docs')

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training Succesful!")
    except Exception as e:
        return Response(f"Error Occured : {e}")

@app.get("/predict")
async def predict_route(data):
    try:
        #data_given = InputData(data).model_dum
        print(f"input data: {type(data)}")
        data_dict = json.loads(data)
        print(data_dict)
        print(type(data_dict))
        #parsed_data = json.loads(data)  # Convert JSON string to dictionary
        df = pd.DataFrame.from_dict(pd.DataFrame(data_dict))
        print(df.head())
        obj = PredictionPipeline()
        predicted_res = obj.predit(df)
        if predicted_res[0] == 0:
            pred = "Not Survived"
        else:
            pred = "Survived"
        return f"Titanic person status is :  {pred}"
    except Exception as e:
        raise e


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1",port=8080)
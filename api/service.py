import pickle

import csv
import pandas as pd
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Request(BaseModel):
    """
    Defines the request schema.
    This means that a client (e.g. the UX backend team)
    will need to send you a json in the format you specify here.

    {
        "temperature": list with 121 entries
    }
    """
    # input fields needed for predictions
    temperature: List[float]
    precipitation: List[float]
    rel_humidity: List[float]
    wind_dir: List[float]
    wind_spd: List[float]
    atmos_press: List[float]


class Response(BaseModel):
    """
    Defines the response schema.
    This is what you will return to the client based on the request.

    The client (UX Backend Team) will receive a json with the following format:

    {
        "air_quality": [ID, PM2.5]
    }
    """

    air_quality: list


@app.get("/")
def health():
    return {"msg": "I'm alive!"}


@app.post("/prediction/", response_model=Response)
def predict_air_quality(request: Request):
    """
    This function defines our air quality prediction endpoint
    """
    # with open("ressources/model.bin", "rb") as model_in:
    #     model = pickle.load(model_in)

    # with open("ressources/encoder.bin", "rb") as encoder_in:
    #     encoder = pickle.load(encoder_in)

    # # get data (json)
    # df = pd.read_json(request.json(), lines=True)

    # # OHE columns of type object
    # df = encoder.transform(df)

    # # predict salaries
    # pred = model.predict(df)
    pred = ["LUKE", "I AM YOUR PREDICTION!"]
    # # return predictions
    return Response(air_quality=pred)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4242)

# Sample input
# {
#     "temperature": list,
#     "precipitation": list,
#     "rel_humidity": list,
#     "wind_dir": list,
#     "wind_spd": list,
# "atmos_press": list
# }
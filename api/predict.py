import pickle
from pathlib import Path

import pandas as pd
import typer


def load_ressources():
    with open("../models/model_final_1.p", "rb") as model_in:
        model = pickle.load(model_in)

    # with open("ressources/encoder.bin", "rb") as encoder_in:
    #     encoder = pickle.load(encoder_in)
    # return encoder, model


app = typer.Typer()

@app.command()
def predict(path: Path):
    """
    Command line command that can be executed with a parameter
    """
    #encoder, 
    model = load_ressources()
    # load data from json at path
    df = pd.read_json(path, lines=True)
    
    # OHE columns of type object
    #df = encoder.transform(df)

    # extract locations and encode
    loc_dummies = pd.get_dummies(df['location'], drop_first=True)
    # add to feature matrix
    df = pd.concat([df, loc_dummies], axis=1)
    # drop location column
    df = df.drop('location', axis=1)

    # predict pm2.5
    prediction = model.predict(df)

    # return predictions
    return prediction
    

if __name__ == "__main__":
    app()

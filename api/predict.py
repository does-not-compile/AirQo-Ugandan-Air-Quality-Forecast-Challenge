import pickle
from pathlib import Path

import pandas as pd
import typer


def load_ressources():
    with open("ressources/model.bin", "rb") as model_in:
        model = pickle.load(model_in)

    with open("ressources/encoder.bin", "rb") as encoder_in:
        encoder = pickle.load(encoder_in)
    return encoder, model


app = typer.Typer()

@app.command()
def predict(path: Path):
    """
    Command line command that can be executed with a parameter
    """
    encoder, model = load_ressources()
    # load data from json at path
    df = pd.read_json(path, lines=True)
    
    # OHE columns of type object
    df = encoder.transform(df)

    # predict salaries
    prediction = model.predict(df)

    # return predictions
    return prediction
    

if __name__ == "__main__":
    app()

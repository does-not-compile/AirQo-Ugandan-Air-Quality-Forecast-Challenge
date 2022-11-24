# AirQo Challange: Forecasting of Ugandan Air Quality

---

This repo is actively being worked on right now. Final models will be available on November 30th, 2022.

---

This challenge was posted on zindi.com with the goal of accurate daily air quality predictions for the general public. Find the challenge website [here](https://zindi.africa/competitions/airqo-ugandan-air-quality-forecast-challenge/data)

## Collaborators

[Jess](https://github.com/JessFinn), [Matthias](https://github.com/NewFishMH), [Samer](https://github.com/samerzahra), [Sebastian](https://github.com/does-not-compile)

---

## Requirements and Environment

Requirements:
- pyenv with Python: 3.9.8

Environment: 

For installing the virtual environment you can either use the Makefile and run `make setup` or install it manually with the following commands: 

```Bash
pyenv local 3.9.8
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

In order to train the model and store test data in the data folder and the model in models run:

```bash
#activate env
source .venv/bin/activate

python example_files/train.py  
```

In order to test that predict works on a test set you created run:

```bash
python example_files/predict.py models/linear_regression_model.sav data/X_test.csv data/y_test.csv
```

## Limitations

Development libraries are part of the production environment, normally these would be separate as the production code should be as slim as possible.

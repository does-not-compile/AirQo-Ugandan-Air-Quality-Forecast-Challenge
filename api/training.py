import pickle

import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV, train_test_split
from xgboost import XGBRegressor

# work_year, experience_level, employment_type, 
# job_title, salary, salary_currency, salary_in_usd, 
# employee_residence, remote_ratio, company_location, company_size


def train():
    data = pd.read_csv("data/ds_data.csv")
    y = data['salary_in_usd']
    X = data[
        ["experience_level", "employment_type", "company_size", "remote_ratio", "company_location", "employee_residence"]
    ]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    xgb = XGBRegressor()

    params = {}

    grid = GridSearchCV(
        estimator=xgb,
        param_grid=params,
        scoring="neg_mean_squared_error",
        cv=3,
    )
    grid.fit(X_train, y_train)
    y_pred = grid.predict(X_test)

    print(
        f"Best model has the following params:{grid.best_params_} and an RMSE of: {mean_squared_error(y_test, y_pred, squared=False)}"
    )

    with open("ressources/model.bin", "wb") as model_out:
        pickle.dump(grid.best_estimator_, model_out)

if __name__ == "__main__":
    train()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import pickle
import warnings
warnings.filterwarnings('ignore')

from feature_engineering import fill_missing_values, drop_column, transform_altitude

# coffee data
url="https://github.com/jldbc/coffee-quality-database/raw/master/data/robusta_data_cleaned.csv"
coffee_features=pd.read_csv(url)

# coffee score

url="https://raw.githubusercontent.com/jldbc/coffee-quality-database/master/data/robusta_ratings_raw.csv"
coffee_quality=pd.read_csv(url)


#cleaning data and preparing
Y = coffee_quality["quality_score"]
X = coffee_features.select_dtypes(['number'])


# splittin into train and test
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.30, random_state=42)
## in order to exemplify how the predict will work.. we will save the y_train
print("Saving test data in the data folder")
X_test.to_csv("data/X_test.csv", index=False)
y_test.to_csv("data/y_test.csv", index=False)

print("Feature engineering on train")
X_train = transform_altitude(X_train)
X_train = drop_column(X_train, col_name='Unnamed: 0')
X_train = drop_column(X_train, col_name='Quakers')
X_train = fill_missing_values(X_train)

# model
print("Training a simple linear regression")
reg = LinearRegression().fit(X_train, y_train)
y_train_pred = reg.predict(X_train)
mse_train = mean_squared_error(y_train, y_train_pred)

#feature eng on test data
print("Feature engineering on test")
X_test = transform_altitude(X_test)
X_test = drop_column(X_test, col_name='Unnamed: 0')
X_test = drop_column(X_test, col_name='Quakers')
X_test = fill_missing_values(X_test)

y_test_pred = reg.predict(X_test)
mse_test = mean_squared_error(y_test, y_test_pred)

print (f"MSE on train is: {mse_train}")
print (f"MSE on test is: {mse_test}")
print("this is obviously fishy")
#saving the model
print("Saving model in the model folder")
filename = 'models/linear_regression_model.sav'
pickle.dump(reg, open(filename, 'wb'))
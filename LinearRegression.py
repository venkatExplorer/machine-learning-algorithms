#Linear Regression

import pandas as pd 

data = pd.read_csv(r"C:\Users\venka\Downloads\data (2).csv")
X = data[["YearsExperience"]]
Y = data["Salary"]

from sklearn.model_selection import train_test_split 
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.33, random_state=42)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

from sklearn.metrics import r2_score

r2 = r2_score(Y_test, Y_pred)
print(r2)


#problems 
# while reading we should place r before path
# pandas module install - pip install pandas
#sklearn module install - pip install scikit-learn
# if we want to run - python LinearRegression.py
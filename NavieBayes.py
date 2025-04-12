#Navie Bayes 

import pandas as pd 

data = pd.read_csv(r"C:\Users\venka\Downloads\diabetes.csv")

Y = data["Outcome"]

X = data.drop("Outcome", axis=1)

from sklearn.model_selection import train_test_split

X_train,X_test, Y_train, Y_test = train_test_split(X,Y, test_size=.30, random_state=42)

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)

from sklearn.metrics import confusion_matrix, accuracy_score

conf_matrix = confusion_matrix(Y_test, Y_pred)
accuracy = accuracy_score(Y_test, Y_pred)

print(conf_matrix)
print(accuracy)




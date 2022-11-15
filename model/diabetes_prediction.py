import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
df = pd.read_csv('Dataset/diabetes.csv')

print(df.shape)

df.isnull().sum()

new_df = df
new_df[["Glucose","BloodPressure","SkinThickness","BMI","Insulin"]] = new_df[["Glucose","BloodPressure","SkinThickness","BMI","Insulin"]].replace(0,np.NaN)


new_df["Glucose"].fillna(new_df["Glucose"].mean(), inplace = True)
new_df["BloodPressure"].fillna(new_df["BloodPressure"].mean(), inplace = True)
new_df["SkinThickness"].fillna(new_df["SkinThickness"].mean(), inplace = True)
new_df["Insulin"].fillna(new_df["Insulin"].mean(), inplace = True)
new_df["BMI"].fillna(new_df["BMI"].mean(), inplace = True)

y = new_df['Outcome']
X = new_df.drop('Outcome', axis=1)

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size = 0.20, random_state = 42, stratify = new_df['Outcome'] )

model = LogisticRegression()
model.fit(X_train, Y_train)
y_predict = model.predict(X_test)

accuracy =accuracy_score(Y_test, y_predict)
print(accuracy)

filename = 'model.pkl'
pickle.dump(model,open(filename,'wb'))

y_predict = model.predict([[1,148,72,35,79.799,33.6,0.35,50]])
print(y_predict)

print("Glucose: "+ str(new_df["Glucose"].mean()))
print("Blood Pressure: "+ str(new_df["BloodPressure"].mean()))
print("SkinThickness: "+ str(new_df["SkinThickness"].mean()))
print("BMI: "+ str(new_df["BMI"].mean()))
print("Insulin: "+ str(new_df["Insulin"].mean()))

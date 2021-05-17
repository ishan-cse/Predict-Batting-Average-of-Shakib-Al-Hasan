import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pandas.read_csv('/content/Dataset_2 (Sakib_Batting_Average).csv')

model = LinearRegression()

model.fit(df[['x']], df[['y']])

print("Enter year which is X")
X = float(input())

Y = model.predict([[X]])

print("Predicted Y = ",Y)

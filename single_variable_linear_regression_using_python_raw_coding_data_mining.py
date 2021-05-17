import pandas as pd

df=pd.read_csv("/content/Dataset_2 (Sakib_Batting_Average).csv")

x,y,x_minus_x_bar,y_minus_y_bar,x_minus_x_bar_mul_y_minus_y_bar,x_minus_x_bar_squre = 0,0,0,0,0,0

for k in range(0,len(df)):
    x = df.at[k,'x'] + x
    y = df.at[k,'y'] + y
    
x_bar = x / len(df.x)
print("X_bar = ",x_bar)

y_bar = y / len(df.y)
print("Y_bar = ",y_bar)

for l in range(0,len(df)):
    x_minus_x_bar = (df.at[l,'x']-x_bar) + x_minus_x_bar
    y_minus_y_bar = (df.at[l,'y']-y_bar) + y_minus_y_bar
    x_minus_x_bar_mul_y_minus_y_bar = ((df.at[l,'x']-x_bar) * (df.at[l,'y'] - y_bar)) + x_minus_x_bar_mul_y_minus_y_bar
    x_minus_x_bar_squre = pow( (df.at[l,'x']-x_bar) , 2 ) + x_minus_x_bar_squre


m = x_minus_x_bar_mul_y_minus_y_bar/x_minus_x_bar_squre
print ("m =",m)

b = y_bar - (m * x_bar)
print ("b =",b)

print()
print("Enter year which is X")
X= float(input())

Y = (m * X) + b

print("Predicted Y = ",Y)

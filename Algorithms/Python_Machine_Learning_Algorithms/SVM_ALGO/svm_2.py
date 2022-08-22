import matplotlib.pyplot as plt 
import pandas as pd

"""
z = x^2 + y^2

Previous Training data into model, Prediction from new model

Id,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species

"""
df = pd.read_csv('/Users/admin65/Desktop/Python_Machine_Learning_Algorithms/SVM_ALGO/iris.csv')
df = df.drop(['Id'],axis=1)
target = df['Species']
s = set()
for val in target:
        s.add(val)
s = list(s)
rows = list(range(100,150))
df = df.drop(df.index[rows])


x = df['SepalWidthCm']
y = df['PetalWidthCm']

setosa_x = x[:50]  #Green
setosa_y = y[:50]  #Green

versicolor_x = x[50:] #Red
versicolor_y = y[50:] #Red

plt.figure(figsize=(8,6))
plt.scatter(setosa_x,setosa_y,marker='+',color='green')
plt.scatter(versicolor_x,versicolor_y, marker='_',color='red')
plt.show()
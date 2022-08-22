import numpy as np
from sklearn.linear_model import LinearRegression


#   
"""
Y = a * X + n
Y - Dependent Variable
a - Slope
X - Indepent variable
b - Intercept
"""

x = np.array([5,15,25,35,45,55]).reshape((-1,1))
y = np.array([5,5,5,5,5,5])

model = LinearRegression()

model.fit(x,y)

model = LinearRegression().fit(x ,y)

r_sq = model.score(x,y)
print(f"coefficient of determination: {r_sq}")
print(f"intercept: {model.intercept_}")
print(f"slope: {model.coef_}")


# y_pred = model.predict(x)
# print(f"predicted response: \n {y_pred}")

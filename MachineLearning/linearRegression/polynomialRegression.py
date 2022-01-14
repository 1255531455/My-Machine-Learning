import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv("degree2.csv")

plt.scatter(df.x, df.y)

model = LinearRegression()

x = df.x[0:6, np.newaxis]   # convert to 2D array
y = df.y[0:6, np.newaxis]   # convert to 2D array

print(x.shape)
model.fit(x, y)

y_pred = model.predict(x)

plt.scatter(x, y, s=10, color='b')

plt.plot(x, y_pred, color='r')


print('R-Squared for training set: %.4f' % model.score(x, y))

# Quadratic polynomial function
degree = 2
polynomial_features = PolynomialFeatures(degree=degree)
# Y = ax+bx^2
x_poly = polynomial_features.fit_transform(x)
print(x_poly)

# training model
model = LinearRegression()
model.fit(x_poly, y)
y_poly_pred = model.predict(x_poly)

plt.figure(2)
# plot the points
plt.scatter(x, y, s=10)

# plot the regression line
plt.plot(x, y_poly_pred)

# 斜率和系数
print('intercept=%f' % model.intercept_)
print('a and b =', model.coef_)

print('R-Squared for training set:%.4f' % model.score(x_poly, y))

# Cubic polynomial function
degree = 3
polynomial_features = PolynomialFeatures(degree=degree)
x_poly = polynomial_features.fit_transform(x)

print(x_poly)

print(polynomial_features.get_feature_names('x'))

model = LinearRegression()
model.fit(x_poly, y)
y_poly_pred = model.predict(x_poly)
plt.figure(3)
plt.scatter(x, y, s=10)

plt.plot(x, y_poly_pred)
plt.xlabel(model.score(x_poly, y))

plt.show()

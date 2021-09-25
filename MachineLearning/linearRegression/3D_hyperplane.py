import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import PolynomialFeatures

dataset = load_boston()

df = pd.DataFrame(dataset.data, columns=dataset.feature_names)


df['MEDV'] = dataset.target


x = pd.DataFrame(np.c_[df['LSTAT'], df['RM']], columns=['LSTAT', ['RM']])
Y = df['MEDV']


# The data set was divided into 70% for training and 30% for testing
x_train, x_test, Y_train, Y_test = train_test_split(x, Y, test_size=0.3, random_state=5)


degree = 2
polynomial_features = PolynomialFeatures(degree=degree)
x_train_poly = polynomial_features.fit_transform(x_train)

# training test model
model = LinearRegression()
model.fit(x_train_poly, Y_train)



# draw 3D image to check correlation
fig = plt.figure(figsize=(18, 15))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df['LSTAT'],
           df['RM'],
           df['MEDV'],
           c='b')
ax.set_xlabel("LSTAT")
ax.set_ylabel("RM")
ax.set_zlabel("MEDV")


# create a meshgrid of all the values for LSTAT and RM
x_surf = np.arange(0, 40, 1)
y_surf = np.arange(0, 10, 1)
x_surf, y_surf = np.meshgrid(x_surf, y_surf)

degree = 2
polynomial_features = PolynomialFeatures(degree=degree)
x_poly = polynomial_features.fit_transform(x)

model = LinearRegression()
model.fit(x_poly, Y)

z = lambda x, y: (model.intercept_ +
                  model.coef_[1] * x +
                  model.coef_[2] * y +
                  model.coef_[3] * x**2 +
                  model.coef_[4] * x*y +
                  model.coef_[5] * y**2)



ax.plot_surface(x_surf, y_surf, z(x_surf, y_surf),
                rstride=1,
                cstride=1,
                color='None',
                alpha=0.4)

"""   """



plt.show()

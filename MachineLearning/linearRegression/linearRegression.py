import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from mpl_toolkits.mplot3d import Axes3D


dataset = load_boston()
# print(dataset)
# print(dataset.feature_names)

# print(dataset.target)

df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
# print(df.head())

# add 'MEDV' target
df['MEDV'] = dataset.target
# print(df.head())

""" data processing """
# df.info()

# check isnull
print(df.isnull().sum())

# correlation judgment
corr = df.corr()
print(corr)

# get top 3 features that has the highest correlation
print(df.corr().abs().nlargest(3, 'MEDV').index)

# draw image
# plt.scatter(df['LSTAT'], df['MEDV'], marker='o')
# plt.xlabel('LSTAT')
# plt.ylabel('MEDV')
# plt.show()

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
# plt.show()
# ax.remove()     # 删除画布上的图像

# training model
x = pd.DataFrame(np.c_[df['LSTAT'], df['RM']], columns=['LSTAT', ['RM']])
Y = df['MEDV']

# create a meshgrid of all the values for LSTAT and RM
x_surf = np.arange(0, 40, 1)
y_surf = np.arange(0, 10, 1)

# training model
model = LinearRegression()
model.fit(x, Y)

x_surf, y_surf = np.meshgrid(x_surf, y_surf)
z = lambda x, y: (model.intercept_ + model.coef_[0] * x + model.coef_[1] * y)

ax.plot_surface(x_surf, y_surf, z(x_surf, y_surf),
                rstride=1,
                cstride=1,
                color='None',
                alpha=0.4)

"""   """


# The data set was divided into 70% for training and 30% for testing
x_train, x_test, Y_train, Y_test = train_test_split(x, Y, test_size=0.3, random_state=5)

# training test model
model = LinearRegression()
model.fit(x_train, Y_train)
price_pred = model.predict(x_test)

print('R-Squared: %.4f' % model.score(x_test, Y_test))

mse = mean_squared_error(Y_test, price_pred)
print(mse)
print(Y_test.shape)
print(price_pred.shape)
plt.figure(2)
plt.scatter(Y_test, price_pred)

plt.xlabel("Actual prices")
plt.ylabel("Predicted prices")
plt.title("Actual prices vs Predicted prices")
plt.show()

# get intercept and gradient
print(model.intercept_)
print(model.coef_)

# use model to predict MEDV when LSTAT=30 and RM=5
print(model.predict([[30, 5]]))

plt.show()

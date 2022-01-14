import random

from sklearn.linear_model import LinearRegression

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.linear_model
from sklearn.preprocessing import PolynomialFeatures

x_data = [338., 333., 328., 207., 226., 25., 179., 60., 208., 606.]
y_data = [640., 633., 619., 393., 428., 27., 193., 66., 226., 1591.]

plt.figure(1)
plt.scatter(x_data, y_data)
# ydata = b + w * xdata

x = np.array(x_data, np.newaxis)
y = np.array(y_data, np.newaxis)
x = x.reshape(10, 1)
y = y.reshape(10, 1)
model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)
plt.plot(x, y_pred, color='r')
print('intercept=%f' % model.intercept_)
print('a and b =', model.coef_)
print('R-Squared for training set:%.4f' % model.score(x, y))


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

plt.figure(3)
# plot the points
plt.scatter(x, y, s=10)
y_poly_pred = np.array(y_poly_pred)
x = np.array(x)
sort_x = x.sort()
sort_y_poly_pred = y_poly_pred.sort()
print(x)
# plot the regression line
plt.plot(sort_x, sort_y_poly_pred)
print(polynomial_features.get_feature_names('x'))
print(y_poly_pred)
print('intercept=%f' % model.intercept_)
print('a and b =', model.coef_)
print('R-Squared for training set:%.4f' % model.score(x_poly, y))

x = np.arange(-200, -100, 1)    # bias
y = np.arange(-5, 5, 0.1)   # weight
z = np.zeros((len(x), len(y)))
for i in range(len(x)):
    for j in range(len(y)):
        b = x[i]
        w = y[j]
        z[j][i] = 0
        for n in range(len(x_data)):
            z[j][i] = z[j][i] + (y_data[n] - b - w*x_data[n])**2    # loss function = 求和(y^ - f(x)) ** 2
        z[j][i] = z[j][i]/len(x_data)

b = random.randint(-200, -100)   # -120 initial b
w = random.randint(-5, 5)  # -4 initial w
lr = 1  # learning rate # 每一次跨的步数
iteration = 100000

# Store initial values for plotting.
b_history = [b]
w_history = [w]

lr_b = 0
lr_w = 0

# Iterations
for i in range(iteration):

    b_grad = 0.0
    w_grad = 0.0
    # 求loss function = 求和(y^ - f(x)) ** 2
    for n in range(len(x_data)):
        b_grad = b_grad - 2.0*(y_data[n] - b - w*x_data[n])*1.0
        w_grad = w_grad - 2.0*(y_data[n] - b - w*x_data[n])*x_data[n]

    lr_b = lr_b + b_grad ** 2
    lr_w = lr_w + w_grad ** 2

    # Updata parameters
    b = b - lr/np.sqrt(lr_b) * b_grad   # 当偏微分趋于零时，达到最值不再变化
    w = w - lr/np.sqrt(lr_w) * w_grad

    # Store paraments for plotting
    b_history.append(b)
    w_history.append(w)
y_pre = []
s = 0
x_data.sort()
y_data.sort()
for i in range(len(x_data)):
    y_pre.append(b+w*x_data[i])
    s += abs(y_pre[i]-y_data[i])

# plot the figure
plt.figure(2)
plt.contourf(x, y, z, 50, alpha=0.5, cmap=plt.get_cmap('jet'))
plt.plot([-188.4], [2.67], 'x', ms=12, markeredgewidth=3, color='orange')
plt.plot(b_history, w_history, 'o-', ms=3, lw=1.5, color='black')
plt.xlim(-200, -100)
plt.ylim(-5, 5)
plt.xlabel(r'$b$', fontsize=16)
plt.ylabel(r'$w$', fontsize=16)

plt.show()

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib
from sklearn.preprocessing import PolynomialFeatures

heights = [[1.6], [1.65], [1.7], [1.73], [1.8]]

weights = [[60], [65], [72.3], [75], [80]]

plt.title('Weights plotted against heights')
plt.xlabel('Heights in meters')
plt.ylabel('Weights in kilograms')

plt.plot(heights, weights, 'k.')

plt.axis([1.5, 1.85, 50, 90])
plt.grid(True)

# 创建线性回归模型
model = LinearRegression()
model.fit(X=heights, y=weights)

# make prediction
# weight = model.predict([[1.75]])[0][0]
# print(round(weight, 2))

# plot the regression line
plt.plot(heights, model.predict(heights), color='r')

# 得到斜率和截距
# plt.axis([0, 1.85, -200, 200])
extreme_heights = [[0], [1.8]]
# plt.plot(extreme_heights, model.predict(extreme_heights), color='b')

# 得到y轴截距
print(round(model.intercept_[0], 2))

# 得到斜率
print(round(model.coef_[0][0], 2))


# 通过计算残差平方和检验模型的性能
print('Residual sum of squares: %.2f' %
      np.sum((weights - model.predict(heights)) ** 2))

# test data
heights_test = [[1.58], [1.62], [1.69], [1.76], [1.82]]
weights_test = [[58], [63], [72], [73], [85]]

# 计算R平方(拟合度)
print('R-squared: %.4f' % model.score(heights_test,
                                      weights_test))


# 持久化模型

# save the model to disk
filename = 'HeightsAndWeights_model2.sav'
joblib.dump(model, filename)

# load the model from disk
loaded_model = joblib.load(filename)

# use model
result = loaded_model.score(heights_test, weights_test)
print("%.4f" % result)

# 2degree
degree = 2
ploynomial_features = PolynomialFeatures(degree=degree)
x_ploy = ploynomial_features.fit_transform(heights)

model = LinearRegression()
model.fit(x_ploy, weights)

y_poly_pred = model.predict(x_ploy)

plt.figure(2)
plt.scatter(heights, weights)
plt.plot(heights, y_poly_pred)
print(model.score(x_ploy, weights))
plt.show()

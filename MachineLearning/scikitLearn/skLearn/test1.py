import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from sklearn.preprocessing import PolynomialFeatures

X, y = make_regression(n_samples=100, n_features=1, noise=4.3)
plt.plot(X, y, 'k.')
plt.grid(True)

# 训练模型
model = LinearRegression()
model.fit(X=X, y=y)

# 画回归线
plt.plot(X, model.predict(X), 'r')
print(model.score(X, y))

# 2degree

plt.figure(2)
plt.plot(X, y, 'k.')
degree = 9
polynomial_features = PolynomialFeatures(degree=degree)
x_poly = polynomial_features.fit_transform(X)

model = LinearRegression()
model.fit(x_poly, y)

y_poly_pred = model.predict(x_poly)

plt.plot(X, y_poly_pred)

print(model.score(x_poly, y))
plt.show()

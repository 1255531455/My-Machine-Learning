import pandas as pd
import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(font_scale=1.2)

data = pd.read_csv('house_sizes_prizes_svm.csv')

sns.lmplot('size', 'price',
           data=data,
           hue='sold',
           palette='Set2',
           fit_reg=False,
           scatter_kws={"s": 50})

# training model
X = data[['size', 'price']].values
y = np.where(data['sold'] == 'y', 1, 0)
model = svm.SVC(kernel='linear').fit(X, y)

# min and max for the first feature
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 0].max() + 1

# step size in the mesh
h = (x_max / x_min) / 20

# make predictions for each of the points in xx,yy
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

z = model.predict(np.c_[xx.ravel(), yy.ravel()])

# draw the result using a color plot
z = z.reshape(xx.shape)
plt.contourf(xx, yy, z, cmap=plt.cm.Blues, alpha=0.3)

plt.xlabel('Size of house')
plt.ylabel('Asking price(1000s)')
plt.title("Size of Houses and Their Asking Prices")


# plt.show()

# prediction
def will_it_sell(size, price):
    if (model.predict([[size, price]])) == 0:
        print('Will mot sell')
    else:
        print('Will sell')


will_it_sell(2500, 400)
will_it_sell(2500, 200)

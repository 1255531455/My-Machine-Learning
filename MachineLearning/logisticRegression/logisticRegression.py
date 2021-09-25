import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
import matplotlib.patches as mpatches
from sklearn.model_selection import train_test_split
from sklearn import linear_model

cancer = load_breast_cancer()

# copy from dataset into a 2-d list
X = []
for target in range(2):  # target means is_get_cancer
    X.append([[], []])
    for i in range(len(cancer.data)):
        if cancer.target[i] == target:
            X[target][0].append(cancer.data[i][0])  # x:mean radius
            X[target][1].append(cancer.data[i][1])  # y:mean texture

colours = ("r", "b")

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
for target in range(2):
    ax.scatter(X[target][0],
               X[target][1],
               c=colours[target])
ax.set_xlabel("mean radius")
ax.set_ylabel("mean texture")
plt.close()

# 使用一个特征训练
plt.figure(2)
x = cancer.data[:, 0]  # mean radius
y = cancer.target
colors = {0: 'red', 1: 'blue'}
plt.scatter(x, y,
            facecolors='none',
            edgecolors=pd.DataFrame(cancer.target)[0].apply(lambda x: colors[x]),
            cmap=colors)

plt.xlabel("mean radius")
plt.ylabel("Result")
red = mpatches.Patch(color='red', label='malignant')
blue = mpatches.Patch(color='blue', label='benign')

plt.legend(handles=[red, blue], loc=1)

# 确定截距和系数

# build model
log_regress = linear_model.LogisticRegression()

# training model
log_regress.fit(X=np.array(x).reshape(len(x), 1),
                y=y)
print(log_regress.intercept_)
print(log_regress.coef_)


# draw sigmoid line
def sigmoid(x):
    return 1 / (1 + np.exp(-(log_regress.intercept_[0] + (log_regress.coef_[0][0] * x))))


x1 = np.arange(0, 30, 0.01)
y1 = [sigmoid(n) for n in x1]
plt.scatter(x, y,
            facecolors='none',
            edgecolors=pd.DataFrame(cancer.target)[0].apply(lambda x: colors[x]),
            cmap=colors)
plt.plot(x1, y1)
plt.xlabel("mean radius")
plt.ylabel("Probability")

# 对所有特性训练模型
train_set, test_set, train_labels, test_labels = train_test_split(cancer.data,
                                                                  cancer.target,
                                                                  test_size=0.25,
                                                                  random_state=1,
                                                                  stratify=cancer.target)

x = train_set[:, 0:30]
y = train_labels
log_regress = linear_model.LogisticRegression()
log_regress.fit(X=x, y=y)

print(log_regress.intercept_)
print(log_regress.coef_)

# test model
preds_prob = pd.DataFrame(log_regress.predict_proba(X=test_set))

preds_prob.columns = ["Malignant", "Benign"]

preds = log_regress.predict(X=test_set)
preds_class = pd.DataFrame(preds)
preds_class.columns = ["Prediction"]

original_result = pd.DataFrame(test_labels)
original_result.columns = ["Original Result"]

result = pd.concat([preds_prob, preds_class, original_result], axis=1)
print(result.head())

# 得到混淆矩阵
print("---Confusion Matrix---")
print(pd.crosstab(preds, test_labels))

#####################################################


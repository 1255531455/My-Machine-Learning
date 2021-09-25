import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset("iris", data_home="C:\\Users\\yangdong\\PycharmProjects\\pythonProject\\venv\\Lib\\site-packages\\seaborn\\seaborn_data")
sns.lmplot('petal_width', 'petal_length', data=iris,
           hue='species', palette='Set1',
           fit_reg=False, scatter_kws={"s": 70})

ax = plt.gca()
ax.set_title("Plotting using the Iris dataset")
plt.show()

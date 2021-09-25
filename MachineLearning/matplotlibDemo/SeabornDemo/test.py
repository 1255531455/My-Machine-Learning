import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("penguins", data_home="C:\\Users\\yangdong\\PycharmProjects\\pythonProject\\venv\\Lib\\site"
                                            "-packages\\seaborn\\seaborn_data")
sns.pairplot(df, hue="species")
plt.show()


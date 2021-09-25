import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

titanic = pd.read_csv("titanic.csv")
g = sns.catplot(x="who", y="survived", col="class",
                data=titanic, kind="bar", ci=None, aspect=1)
g.set_axis_labels("", "Survival Rate")
g.set_xticklabels(["Man", "Women", "Children"])
g.set_titles("{col_name} {col_var}")

plt.show()

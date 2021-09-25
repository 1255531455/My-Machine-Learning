import pandas as pd
# 折线图
import matplotlib.pyplot as plt
from matplotlib import style
# 样式

style.use("ggplot")
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
         [2, 4.5, 1, 2, 3.5, 2, 1, 2, 3, 2],
         label="Jim")   # 添加图例

# 绘制多条折线图
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
         [3, 5.5, 2, 3, 4.5, 3, 2, 3, 4, 3],
         label="Tom")
# 添加标题
plt.title("Results")
plt.xlabel("Semester")
plt.ylabel("Grade")
plt.legend()    # 添加图例
plt.show()




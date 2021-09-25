# 柱状图
import matplotlib.pyplot as plt
from matplotlib import style

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
          'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
# 样式

style.use("ggplot")
plt.bar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        months,
        label="Jim",  # 添加图例
        color="m",
        align="center",  # 柱状图
        alpha=0.5  # 透明度为0.5
        )

# 绘制多条折线图
plt.bar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        months,
        label="Tom",
        color="m",
        align="center",  # 柱状图
        alpha=0.5  # 透明度为0.5
        )
# 添加标题
plt.title("Results")
plt.xlabel("Semester")
plt.ylabel("Grade")
plt.legend()  # 添加图例
plt.grid(True, color="y")
plt.show()
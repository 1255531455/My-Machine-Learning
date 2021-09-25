import matplotlib.pylab as plt

labels = ["Chrome", "Internet Explorer",
          "Firefox", "Edge", "Safari",
          "Sago Explorer", "Opera", "Others"]
marketShare = [61.64, 11.98, 11.02, 4.23, 3.79, 1.63, 1.52, 4.19]
explode = (0, 0, 0.5, 0, 0.8, 0, 0, 0)
pie = plt.pie(marketShare,
              explode=explode,
              labels=labels,
              autopct="%.lf%%",
              shadow=True,
              startangle=45)
plt.axis("equal")
plt.title("Web Browser MarketShare - 2018")
plt.legend(pie[0], labels, loc="best")  # 显示图例
plt.savefig("Browsers.png", bbox_inches="tight")     # 保存图片
plt.show()

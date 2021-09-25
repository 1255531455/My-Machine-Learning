from datetime import datetime

import numpy as np
import pandas as pd
import math

""" Pandas Series """

series = pd.Series([1, 2, 3, 4, 5])
print(series)

# 使用指定索引创建Series
print("\n # 使用指定索引创建Series \n")
series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'c'])
print(series)

# 访问Series中的元素
print("\n # 访问Series中的元素 \n")
print(series[2])
print(series.iloc[2])
print(series['d'])
print(series.loc['d'])

print(series['c'])

print(series[2:])

# 指定Datetime范围作为Series的索引
print("\n # 指定Datetime范围作为Series的索引 \n")
dates1 = pd.date_range('20210917', periods=5)
print(dates1)

series = pd.Series([1, 2, 3, 4, 5])
series.index = dates1
print(series)

# 日期范围
print("\n # 日期范围 \n")
dates2 = pd.date_range('20210917', periods=5, freq='M')  # 按每月最后一天跳跃
print(dates2)

dates2 = pd.date_range('20210917', periods=5, freq='MS')  # 按每月第一天跳跃
print(dates2)

""" Pandas DataFrame """

# 创建 DataFrame
print("\n # 创建 DataFrame \n")
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABED'))
print(df)

# 将CSV文件加载到DataFrame中
print("\n # 将CSV文件加载到DataFrame中 \n")
df = pd.read_csv('data.csv')
days = pd.date_range('20210917', periods=10)
df.index = days  # 添加索引
print(df)
print(df.index)  # 获得索引
print(df.values)  # 获得表

# 生成DataFrame的描述性统计信息
print("\n # 生成DataFrame的描述性统计信息 \n")
print(df.describe())

print(df.mean(0))  # 每一列的平均值
print(df.mean(1))  # 每一行的平均值

# 从DataFrame中提取
print("\n # 从DataFrame中提取 \n")
print(df.head(8))  # 输出前八行
print(df.tail(5))  # 输出后五行

# 选择DataFrame中的特定列
print("\n # 选择DataFrame中的特定列 \n")
print(df['A'])  # 选中A列，same as print(df.A)
print(df[['A', 'B']])  # 选中A，B列

# 基于行号的切片
print("\n # 基于行号的切片 \n")
print(df[2:4])  # 从DataFrame中提取2~4行(不包括第四行)

print(df.iloc[[2, 4]])  # 输出第二行和第四行

print(df.iloc[4])  # 输出第四行

# 基于行号和列号的切片
print("\n # 基于行号和列号的切片 \n")
print(df.iloc[2:4, 1:4])  # 输出第二行到第三行，第一列到第三列
print(df.iloc[[2, 4], [1, 3]])  # 输出行号2和4，列号1和3

# 根据标签进行切片
print("\n # 根据标签进行切片 \n")
print(df)
print(df.loc['20210917':'20210921'])  # 按时间标签提取
print(df.loc['20210917':'20210921', 'A':'C'])  # 按时间标签和标题提取
print(df.loc['20210917':'20210921', ['A', 'C']])  # 提取特定的行
print(df.loc['20210920'])  # 提取特定的行

# 需要提取以datetime为索引的特定行时，需要将日期装换成datetime格式
date1 = datetime(2021, 9, 17, 0, 0, 0)
date2 = datetime(2021, 9, 21, 0, 0, 0)
print(df.loc[[date1, date2]])

# 选中单个单元格
# print(df.at[date1, 'B'])

# 转置DataFrame
print(df.transpose())


# 检查结果是DataFrame还是series
def checkSeriesOrDataframe(var):
    if isinstance(var, pd.DataFrame):
        return 'DataFrame'
    if isinstance(var, pd.Series):
        return 'Series'


print(checkSeriesOrDataframe(df))

# 在DataFrame中排序数据
# 通过索引排序
print(df.sort_index(axis=0, ascending=False))

# 按列标签排序
print(df.sort_index(axis=1, ascending=False))

# 按值排序
print(df.sort_values('A', axis=0))  # 对A列的值升序排列

# 指定特定索引
print(df.sort_values('20210917', axis=1))

# 将函数应用于DataFrame
sq_root = lambda x: math.sqrt(x) if x > 0 else x  # 平方根
sq = lambda x: x ** 2  # 平方
print(df.B.apply(sq_root))  # 将sq_root运用与B
print(df.apply(sq))  # 将sq运用与DataFrame

# print(df.apply(sq_root))报错ValueError
# 将sq_root应用于整个DataFrame中，可用遍历
for column in df:
    df[column] = df[column].apply(sq_root)
print(df)

# 将每一列相加
print(df.apply(np.sum, axis=0))

# 将每一行相加
print(df.apply(np.sum, axis=1))

""" 在DataFrame中添加和删除行和列 """
print(df)
# 添加列
E = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
df["E"] = E
print(df)
# 删除行
print(df.drop(['20210917'], inplace=True))   # 删除一行 inplace参数可用于修改原DataFrame

# 删除指定一行
print(df.drop(df.index[1]))  # 删除了第二行

# 删除列
print(df.drop('E', axis=1))     # 删除了E列
# 删除指定一列
print(df.drop(df.columns[1], axis=1))   # 删除了第二列

# 生成交叉表
print(pd.crosstab(df.A, df.B))


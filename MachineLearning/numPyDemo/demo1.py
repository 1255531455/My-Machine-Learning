""" 创建numpy数组 """
import numpy as np

a1 = np.arange(10)
print(a1)

a2 = np.arange(0, 10, 2)
print(a2)

a3 = np.zeros(5)
print(a3)
print(a3.shape)

a4 = np.zeros((2, 3))
print(a4)
print(a4.shape)

a5 = np.full((2, 3), 3)
print(a5)

a6 = np.eye(3)
print(a6)

a7 = np.random.random((2, 4))
print(a7)

list1 = [1, 2, 3, 4, 5]
r1 = np.array(list1)
print(r1)

""" 数组索引 """
print(r1[0])
print(r1[1])

list2 = [6, 7, 8, 9, 0]
r2 = np.array([list1, list2])
print(r2)
print(r2.shape)
print(r2[0, 0])
print(r2[0, 1])

r3 = np.array(list1)
print(r3[[2, 4]])

"""" 布尔索引 """
print(r1 > 2)

print(r1[r1 > 2])

nums = np.arange(20)
print(nums)
odd_num = nums[nums % 2 == 1]
print(odd_num)

"""" 切片数组p24 """
a = np.array([[1, 2, 3, 4, 5],
              [4, 5, 6, 7, 8],
              [9, 8, 7, 6, 5]])
print(a)

b1 = a[1:3, :3]
b2 = a[1:2, :2]
print(b1)
print(b2)

"""" 重塑数组 """
b1 = b1.reshape(1, -1)
print(b1)

"""" 数组数学 """
names = np.array(['ann', 'joe', 'mark'])
heights = np.array([1.5, 1.78, 1.6])
weights = np.array([65, 46, 59])
bmi = weights / heights ** 2
print(bmi)
print("Overweight:", names[bmi > 25])

x = np.array([2, 3])
y = np.array([4, 2])
np.dot(x, y)  # 点积 2*4+3*2=14

""" 矩阵 """
x2 = np.matrix([[1, 2],
                [4, 5]])
# 求和
print(a.cumsum(axis=0))

"""" 排序 """
ages = np.array([34, 12, 37, 5, 13])
sorted_ages = np.sort(ages)  # 将排序好的传给sorted_ages
ages.sort()     # 直接排序
indx = np.argsort(ages) # [::-1] 按降序排列     # 得到序列
print(ages[indx])       # 按序列排序

""" 引用复制 """

# 深度复制
a2 = a1.copy()
# 浅复制
a2 = a1.view()
#赋值
a2 = a1
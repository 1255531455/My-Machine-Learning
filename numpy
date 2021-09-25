""" Create numpy array """
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

""" Array index """
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

"""" Boolean index """
print(r1 > 2)

print(r1[r1 > 2])

nums = np.arange(20)
print(nums)
odd_num = nums[nums % 2 == 1]
print(odd_num)

"""" Slice array """
a = np.array([[1, 2, 3, 4, 5],
              [4, 5, 6, 7, 8],
              [9, 8, 7, 6, 5]])
print(a)

b1 = a[1:3, :3]
b2 = a[1:2, :2]
print(b1)
print(b2)

"""" Reshape array """
b1 = b1.reshape(1, -1)
print(b1)

"""" Array mathematics """
names = np.array(['ann', 'joe', 'mark'])
heights = np.array([1.5, 1.78, 1.6])
weights = np.array([65, 46, 59])
bmi = weights / heights ** 2
print(bmi)
print("Overweight:", names[bmi > 25])

x = np.array([2, 3])
y = np.array([4, 2])
np.dot(x, y)  # 点积 2*4+3*2=14

""" Matrix """
x2 = np.matrix([[1, 2],
                [4, 5]])
# sum
print(a.cumsum(axis=0))

"""" sort """
ages = np.array([34, 12, 37, 5, 13])
sorted_ages = np.sort(ages)  
ages.sort()     
indx = np.argsort(ages) 
print(ages[indx])       

""" copy """


a2 = a1.copy()

a2 = a1.view()

a2 = a1

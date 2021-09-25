import matplotlib.pyplot as plt

plt.subplot(121)
plt.plot([1, 2, 3, 4],
         [1, 8, 27, 64],
         'bo')  # blue circle
plt.subplot(122)
plt.plot([2, 3, 4, 4.5],
         [2, 9, 30, 69],
         'y^')
plt.axis([0, 4.5, 0, 70])
plt.show()

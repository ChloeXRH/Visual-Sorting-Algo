import random
import matplotlib.pyplot as plt


data = [random.randint(0, 100) for i in range(75)]
array = data

n = len(array)

for i in range(n-1):
    for j in range(n-i-1):
        plt.bar(range(n),array)
        plt.pause(0.01)
        plt.clf()
        if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                print(array)

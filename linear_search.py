import numpy as np

def linear(arr, target):
    for i in arr: 
        if i == target:
            return i
    return -1

arr = np.loadtxt("sorted_array.txt", dtype=int, delimiter=',')
print(linear(arr,2000))
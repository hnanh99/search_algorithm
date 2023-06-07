import numpy as np

def binary(arr, target, left, right):
    mid = (right + left) // 2
    
    if len(arr) < 2:
        return -1
    
    if (arr[mid] == target):
        return mid
    
    elif (target > arr[mid]):
        return binary(arr, target, mid + 1, right)
    else: 
        return binary(arr, target, left, mid-1)

arr = np.loadtxt("sorted_array.txt", dtype=int, delimiter=',')
print(binary(arr,2000,0,len(arr)))
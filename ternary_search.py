import numpy as np

def ternary(arr, target, left, right):
    while (len(arr) > 1):
        partition = (right-left)//3
        mid1 = left + partition
        mid2 = right - partition
        
        if (target == arr[mid1]):
            return mid1
        elif (target == arr[mid2]):
            return mid2
        elif (target < arr[mid1]):
            r = mid1-1
        elif (target > arr[mid2]):
            l = mid2+1
        else:
            l = mid1+1
            r = mid2-1
    return -1
arr = np.loadtxt("sorted_array.txt", dtype=int, delimiter=',')

print(ternary(arr,2000,0,len(arr)))
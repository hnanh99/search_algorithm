import numpy as np

def interpolation(arr, target):
    left = 0
    right = len(arr) - 1
    
    while (left <= right & target >= arr[left] & target <=arr[right]):
        var1 = (target - arr[left])/(arr[right]-arr[left])
        var2 = right - left
        pivot = int(left + var1*var2)
        if arr[pivot] == target:
            return pivot
        if arr[pivot] < target:
            left = pivot + 1
        else:
            right = pivot - 1
    return -1
arr = np.loadtxt("sorted_array.txt", dtype=int, delimiter=',')
print(interpolation(arr,2000))
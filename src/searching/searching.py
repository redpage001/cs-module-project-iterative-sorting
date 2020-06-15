import math

def linear_search(arr, target):
    # Your code here
    for index, item in enumerate(arr):
        if item == target:
            return index
            
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    if len(arr) == 0:
        return -1
    
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = math.floor((low + high)/2)
        if arr[middle] < target:
            low = middle + 1
        elif arr[middle] > target:
            high = middle - 1
        else:
            return middle

    return -1  # not found

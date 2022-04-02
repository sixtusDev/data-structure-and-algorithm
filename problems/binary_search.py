from math import floor


def binary_search(arr, target):
    right = len(arr) - 1
    left = 0

    while left < right:
        mid = floor((right + left) / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else: 
            left = mid + 1
    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7], 10))
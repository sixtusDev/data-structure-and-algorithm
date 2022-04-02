# Given a sorted array of numbers, find if a given number ‘key’ is present in the array. 
# Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. 
# You should assume that the array can have duplicates.
# Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1

def binary_search(arr, target):
    right = len(arr) - 1
    left = 0
    is_ascending = arr[0] < len(arr) - 1

    while left <= right:
        mid = (right + left) // 2

        if arr[mid] == target:
            return mid

        if is_ascending:
            if target > arr[mid]:
                left = mid + 1
            else: 
                right = mid - 1
        else:
            if target > arr[mid]:
                right = mid - 1
            else: 
                left = mid + 1

    return -1

print(binary_search([7, 6, 5, 4, 3, 2, 1], 5))
# Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. 
# The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.
# Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1

def ceiling_of_a_number(arr, target):
    left = 0
    right = len(arr) - 1

    if target > arr[right]:
        return -1

    while left <= right:
        mid = (left + right) // 2

        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            return mid

    return left


print(ceiling_of_a_number([4, 6, 10], -1))
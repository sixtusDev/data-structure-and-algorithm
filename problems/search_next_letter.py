# Given an array of lowercase letters sorted in ascending order, 
# find the smallest letter in the given array greater than a given ‘key’.
# Assume the given array is a circular list, which means that the last letter
# is assumed to be connected with the first letter. This also means that the smallest letter
# in the given array is greater than the last letter of the array and is also the first letter of the array.
# Write a function to return the next letter of the given ‘key’


def search_next_letter(arr, target):
    left = 0
    right = len(arr) - 1

    if target >= arr[right] or target <= arr[left]:
        return arr[left]

    while left + 1 < right:
        mid = (left + right) // 2
        if target >= arr[mid]:
            left = mid
        else:
            right = mid

    return arr[right]


print(search_next_letter(['a', 'c', 'f', 'h'], "h"))
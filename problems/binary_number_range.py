# Given an array of numbers sorted in ascending order, find the range of a given number ‘key’.
#  The range of the ‘key’ will be the first and last position of the ‘key’ in the array.
# Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

def find_range(arr, key):
    result = [-1, -1]
    result[0] = binary_search(arr, key, True)
    if result[0] != -1:
        result[1] = binary_search(arr, key, False)

    return result
            
def binary_search(arr, key, find_min_index):
    left = 0
    right = len(arr) - 1
    key_index = -1
    
    while left <= right:
        mid = (left + right) // 2
        if key > arr[mid]:
            left = mid + 1
        elif key < arr[mid]:
            right = mid - 1
        else:
            key_index = mid
            if find_min_index:
                right = right - 1
            else:
                left = left + 1

    return key_index

def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))

main()
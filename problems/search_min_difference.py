# Given an array of numbers sorted in ascending order, find the element
# in the array that has the minimum difference with the given ‘key’.

def min_differnce(arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if key > arr[mid]:
            left = mid + 1
        elif key < arr[mid]:
            right = mid - 1
        else:
            return arr[mid]

    return arr[right]

def main():
    print(min_differnce([4, 6, 10], 7))
    print(min_differnce([4, 6, 10], 4))
    print(min_differnce([1, 3, 8, 10, 15], 12))
    print(min_differnce([4, 6, 10], 17))

main()
def search_bitonic_array(arr, key):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if key > arr[mid] and arr[mid] > arr[mid + 1]:
            left = mid + 1
        elif key > arr[mid] and arr[mid] < arr[mid + 1]:
            right = mid
        elif key < arr[mid] and arr[mid] > arr[mid + 1]:
            right = mid - 1
        elif key < arr[mid] and arr[mid] < arr[mid + 1]:
            left = mid
        else:
            return arr[mid]

    return -1

def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))

main()
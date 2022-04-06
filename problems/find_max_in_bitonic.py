# Find the maximum value in a given Bitonic array. An array is considered bitonic if it is
# monotonically increasing and then monotonically decreasing. Monotonically increasing or 
# decreasing means that for any index i in the array arr[i] != arr[i+1]

def find_max_in_bitonic(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
        
    return arr[left]

def main():
    print(find_max_in_bitonic([1, 3, 8, 12, 4, 2]))
    print(find_max_in_bitonic([3, 8, 3, 1]))

main()
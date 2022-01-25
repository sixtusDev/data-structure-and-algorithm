def binary_search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (high + low) // 2
        if list[mid] == target:
            return True
        if target > list[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return False

print(binary_search([1,2,4,5,6,7,8,10], 6))
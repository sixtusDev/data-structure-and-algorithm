def cyclic_sort(nums):
    i = 0

    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != i + 1:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i = i + 1
    return nums

print(cyclic_sort([1, 5, 6, 4, 3, 2]))
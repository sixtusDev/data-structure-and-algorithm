def find_duplicate(nums):

    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i = i + 1

    for i in range(len(nums)):
        if i + 1 != nums[i]:
            return nums[i]

print(find_duplicate([1, 4, 4, 3, 2]))
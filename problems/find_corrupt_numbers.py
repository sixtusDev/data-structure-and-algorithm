def find_corrupt_numbers(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i = i + 1

    for i in range(len(nums)):
        if i + 1 != nums[i]:
            return [nums[i], i + 1]

print(find_corrupt_numbers([3, 1, 2, 5, 2]))
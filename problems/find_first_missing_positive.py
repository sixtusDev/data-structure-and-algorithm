def find_first_missing_positive(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i = i + 1
    
    for i in range(len(nums)):
        if i + 1 != nums[i]:
            return i + 1

print(find_first_missing_positive([3, 2, 5, 1]))
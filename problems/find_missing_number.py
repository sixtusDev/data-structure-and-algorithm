def find_missing_number(nums):

    i = 0
    while i < len(nums):
        j = nums[i]
        if j < len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i = i + 1
        
    for i in range(len(nums)):
        if nums[i] != i:
            return i


print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
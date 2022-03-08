def find_all_missing_numbers(nums):
    nums.sort()
    non_dup_nums = [nums[0]]
    missing_nums = []

    for i in range(1, len(nums)):
        num = nums[i]
        if non_dup_nums[-1] != num:
            non_dup_nums.append(num)
    
    
    i = 0
    j = 0
    print(non_dup_nums)
    while i < len(non_dup_nums):
        while non_dup_nums[i] != j + 1:
            missing_nums.append(j + 1)
            j = j + 1

        i = i + 1
        j = j + 1
    
    return missing_nums

print(find_all_missing_numbers([2, 3, 2, 1]))

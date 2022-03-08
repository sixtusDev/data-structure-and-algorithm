def find_all_missing_numbers(nums):
    output = []
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
           nums[i], nums[j] = nums[j], nums[i]
        else:
            i = i + 1

    for i in range(len(nums)):
        if i + 1 != nums[i]:
            output.append(i + 1)
    return output

print(find_all_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))

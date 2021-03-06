def find_all_duplicates(nums):
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
            output.append(nums[i])

    return output

print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))
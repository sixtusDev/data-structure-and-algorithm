def find_first_k_missing_number(nums, k):
    output = []
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i = i + 1

    for i in range(len(nums)):
        if i + 1 != nums[i]:
            output.append(i + 1)
        if i == len(nums) - 1:
            if i + 2 in nums:
                output.append(i + 3)
            else:
                output.append(nums[-1] + 1)

    while len(output) < k:
        output.append(output[-1] + 1)

    return output

print(find_first_k_missing_number([-2, -3, 4], 3))
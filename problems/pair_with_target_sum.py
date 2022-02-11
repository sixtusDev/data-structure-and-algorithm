def pair_with_target_sum(array, target_sum):
    left_pointer = 0
    right_pointer = len(array) - 1

    while left_pointer < right_pointer:
        left_item = array[left_pointer]
        right_item = array[right_pointer]
        current_sum = left_item + right_item

        if current_sum < target_sum:
            left_pointer += 1
        elif current_sum > target_sum:
            right_pointer -= 1
        else:
            return [left_pointer, right_pointer]

    return False

print(pair_with_target_sum([2, 5, 9, 11], 11))


        
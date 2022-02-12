def square_sorted_array(array):
    array_len = len(array)
    squares = [0 for _ in range(array_len)]
    index_fixer = array_len - 1
    last_index = array_len - 1
    first_index = 0

    while first_index < last_index:
        left_item_squared = array[first_index] * array[first_index]
        right_item_squared = array[last_index] * array[last_index]

        if left_item_squared > right_item_squared:
            squares[index_fixer] = left_item_squared
            first_index += 1
            index_fixer -= 1
        else:
            squares[index_fixer] = right_item_squared
            last_index -= 1
            index_fixer -= 1

    return squares

print(square_sorted_array([-3, -1, 0, 1, 2]))
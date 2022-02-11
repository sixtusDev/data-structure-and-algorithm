def remove_duplicates(array):
    next_non_duplicate = 1
    i = 1

    while i < len(array):
        if array[next_non_duplicate - 1] != array[i]:
            array[next_non_duplicate] = array[i]
            next_non_duplicate += 1
            i += 1
        else:
            i += 1

    return next_non_duplicate

print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))

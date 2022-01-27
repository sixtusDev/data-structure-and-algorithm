def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left_array = array[:mid]
    right_array = array[mid:]

    left_array = merge_sort(left_array)
    right_array = merge_sort(right_array)

    return merge_two_sorted_list(left_array, right_array)


def merge_two_sorted_list(list1, list2):
    sorted_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            sorted_list.append(list1[i])
            i += 1
        else:
            sorted_list.append(list2[j])
            j += 1

        while i < len(list1):
            sorted_list.append(list1[i])
            i += 1
        while j < len(list2):
            sorted_list.append(list2[j])
            j += 1

    return sorted_list

# print(merge_sort([10, 56, 90, 10, 3, 0, 2, 12]))
print(merge_sort([10, 3, 15, 7, 8, 23, 98, 29]))
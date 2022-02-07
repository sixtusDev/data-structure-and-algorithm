def find_average_of_sub_arrays(array, k):
    result = []
    window_sum = 0.0
    window_start = 0

    for window_end in range(len(array)):
        window_sum += array[window_end]

        if window_end >= k - 1:
            result.append(window_sum / k)
            window_sum -= array[window_start]
            window_start += 1
    return result

result = find_average_of_sub_arrays([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
print(result)
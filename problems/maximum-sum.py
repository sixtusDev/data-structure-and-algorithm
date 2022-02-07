def maximum_sum(array, k):
    window_start = 0
    current_sum = 0
    max_sum = 0

    for window_end in range(len(array)):
        current_sum += array[window_end]

        if window_end >= k - 1:
            max_sum = max(max_sum, current_sum)
            current_sum -= array[window_start]
            window_start += 1

    return max_sum

max_sum = maximum_sum([2,1,5,1,3,2], 3)
print(max_sum)
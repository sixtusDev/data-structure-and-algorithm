def length_of_longest_substring(str, k):
    window_start = 0
    max_len = 0
    count_0 = 0

    for window_end in range(len(str)):
        right_char = str[window_end]

        if right_char == 0:
            count_0 += 1
        
        while count_0 > k:
            left_char = str[window_start]
            if left_char == 0:
                count_0 -= 1
            window_start += 1

        max_len = max(max_len, window_end + 1 - window_start)

    return max_len

print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
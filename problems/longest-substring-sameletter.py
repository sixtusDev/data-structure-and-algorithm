def longest_substring_after_replacement(str, k):
    window_start = 0
    lookup_table = {}
    max_len = 0
    max_frequexncy = 0

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in lookup_table:
            lookup_table[right_char] += 1
        else:
            lookup_table[right_char] = 1
        max_frequexncy = max(max_frequexncy, lookup_table[right_char])

        # condition
        while (window_end + 1 - window_start) - max_frequexncy > k:
            left_char = str[window_start]
            lookup_table[left_char] -= 1
            window_start += 1

        max_len = max(max_len, window_end + 1 - window_start)

    return max_len


print(longest_substring_after_replacement("abccde", 1))
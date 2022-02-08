def longest_substring_with_k_distinct(str, k):
    lookup_table = {}
    window_start = 0
    max_len = 0

    for window_end in range(len(str)):
        if str[window_end] not in lookup_table:
            lookup_table[str[window_end]] = 1
        else:
            lookup_table[str[window_end]] += 1

        while len(lookup_table) > k:
            if lookup_table[str[window_start]] == 1:
                del lookup_table[str[window_start]]
            else:
                lookup_table[str[window_start]] -= 1
            window_start += 1
        
        max_len = max(max_len, window_end + 1 - window_start)
    print(lookup_table)
    return max_len

print(longest_substring_with_k_distinct("cbbebi",3))
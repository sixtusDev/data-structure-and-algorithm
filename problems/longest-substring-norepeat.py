from turtle import right


def non_repeat_substring(str):
    window_start = 0
    lookup_table = {}
    max_len = 0

    for window_end in range(len(str)):
        right_char = str[window_end]

        if right_char in lookup_table:
            lookup_table[right_char] += 1
        else:
            lookup_table[right_char] = 1

        while lookup_table[right_char] >= 2:
            left_char = str[window_start]

            if lookup_table[left_char] == 1:
                del lookup_table[left_char]
            else:
                lookup_table[left_char] -= 1

            window_start += 1

        max_len = max(max_len, window_end + 1 - window_start)
    return max_len

print(non_repeat_sunstring("abccde"))
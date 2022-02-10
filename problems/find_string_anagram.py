def is_permutation(str1, str2):
    str1_ascii_len = 0
    str2_ascci_len = 0

    for char in str1:
        str1_ascii_len += ord(char)
    for char in str2:
        str2_ascci_len += ord(char)

    return str1_ascii_len == str2_ascci_len

def find_string_anagram(str, pattern):
    window_start = 0
    result = []

    for window_end in range(len(str)):
        sub_string = str[window_start: window_end + 1]

        if is_permutation(sub_string, pattern):
            result.append(window_start)

        if len(sub_string) >= len(pattern):
            window_start += 1


    return result

print(find_string_anagram("abbcabc", "abc"))
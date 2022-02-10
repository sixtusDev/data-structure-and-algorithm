def check_permutation(str1, str2):
    str1_ascii_len = 0
    str2_ascii_len = 0

    for char in str1:
        str1_ascii_len += ord(char)
    
    for char in str2:
        str2_ascii_len += ord(char)

    return str1_ascii_len == str2_ascii_len


def string_permutation(str, pattern):
    window_start = 0

    for window_end in range(len(str)):
        sub_string = str[window_start:window_end + 1]
        print(sub_string)

        if len(sub_string) >= len(pattern):
            window_start += 1
        
        if check_permutation(sub_string, pattern):
            return True            

    return False

print(string_permutation("odicf", "dc"))


def string_compression(string):
    current_char = string[0]
    char_count = 0
    compressed_string = ""

    for i in range(len(string)):
        if current_char == string[i]:
            char_count += 1
        else:
            compress = string[i - 1] + str(char_count)
            print(compress)
            compressed_string += compress
            current_char = string[i]
            char_count = 1

        if i + 1 == len(string):
            compressed_string += string[i] + str(char_count)
    
    return compressed_string if len(compressed_string) < len(string) else string

print(string_compression("aabcccccaabaa"))

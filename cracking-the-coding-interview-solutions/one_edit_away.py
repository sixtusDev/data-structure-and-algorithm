def one_edit_away(stringA, stringB):
    char_count = {}
    remaining_char = ""

    for char in stringA:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in stringB:
        if char in char_count:
            if char_count[char] > 1:
                char_count[char] -= 1
            else:
                del char_count[char]
        else:
            remaining_char += char
    print(char_count)
    if len(char_count) == 0 and len(remaining_char) == 1:
        return True
    elif (len(char) == 1 and len(remaining_char) == 0) or (len(char) == 1 and len(remaining_char) == 1):
        return True
    else:
        return False
    
print(one_edit_away("pales", "pale"))
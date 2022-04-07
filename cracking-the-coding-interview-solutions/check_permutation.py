# Given two strings, write a method to decide if one is a permutation of the other.

def check_permutation_using_hash_map(stringA, stringB):
    if len(stringA) != len(stringB):
        return False

    char_ocurrence = {}
    for char in stringA:
        if char in char_ocurrence:
            char_ocurrence[char] += 1
        else:
            char_ocurrence[char] = 1

    for char in stringB:
        if char not in char_ocurrence:
            return False
        if char in char_ocurrence:
            if char_ocurrence[char] == 1:
                del char_ocurrence[char]
            else:
                char_ocurrence[char] -= 1
    
    return False if len(char_ocurrence) > 0 else True

def check_permutation_using_ascii(stringA, stringB):
    if len(stringA) != len(stringB):
        return False
    
    ascii_characters = [0]*128

    for char in stringA:
        ascii_characters[ord(char)] += 1

    for char in stringB:
        ascii_characters[ord(char)] -= 1
        if ascii_characters[ord(char)] < 0:
            return False

    return True

def main():
    print(check_permutation_using_hash_map("abc", "bca"))
    print(check_permutation_using_ascii("abc", "csa"))

main()
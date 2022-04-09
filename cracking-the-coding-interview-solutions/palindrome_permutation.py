# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco catJJ, "atco ctaJJ, etc.)

def palindrome_permutation_using_hash_map(string):
    string = string.lower().replace(" ", "")

    char_occurences = {}

    for char in string:
        if char in char_occurences:
            char_occurences[char] += 1
        else:
            char_occurences[char] = 1

    odd_occurence = 0
    for _, value in char_occurences.items():
        if value % 2 != 0:
            odd_occurence += 1
        if odd_occurence > 1:
            return False

    return True

def palindrome_permutation_using_bit_vector(string):
    string = string.lower().replace(" ", "")

    # Assuming all characters in string are ASCII
    char_XOR = [0] * 128

    for char in string:
        char_XOR[ord(char)] =  char_XOR[ord(char)] ^ 1

    odd_occurence = 0
    for bit in char_XOR:
        if bit == 1:
            odd_occurence += 1
        if odd_occurence > 1:
            return False
    return True

print(palindrome_permutation_using_hash_map("Tact Coa"))
print(palindrome_permutation_using_bit_vector("Tact cCoa"))
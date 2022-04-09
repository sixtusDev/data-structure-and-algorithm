# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco catJJ, "atco ctaJJ, etc.)

def palindrome_permutation(string):
    string = string.lower().replace(" ", "")

    char_occurences = {}

    for char in string:
        if char in char_occurences:
            char_occurences[char] += 1
        else:
            char_occurences[char] = 1

    odd_occurencence = 0
    for _, value in char_occurences.items():
        if value % 2 != 0:
            odd_occurencence += 1
        if odd_occurencence > 1:
            return False

    return True

print(palindrome_permutation("Tact Coa"))
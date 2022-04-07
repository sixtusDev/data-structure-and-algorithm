# Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures

def isUnique(string):
    characters = [None] * 128

    for i in string:
        if characters[ord(i)]:
            return False
        characters[ord(i)] = True

    return True

print(isUnique("abcdeffgh"))
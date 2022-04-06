# Given an array of n-1n−1 integers in the range from 11 to nn, find the one number that is missing from the array.

def find_missing_number1(arr):
    n = len(arr) + 1
    sum = 0

    for i in range(1, n + 1):
        sum += i
    
    for i in arr:
        sum -= i

    return sum

def find_missing_number_usingXOR(arr):
    n = len(arr) + 1
    x1 = 1
    for i in range(2, n + 1):
        x1 = x1 ^ i

    x2 = arr[0]
    for i in range(1, len(arr)):
        x2 = x2 ^ arr[i]
    
    return x1 ^ x2

def main():
    print(find_missing_number1([1, 5, 2, 6, 4]))
    print(find_missing_number_usingXOR([1, 5, 2, 6, 4]))

main()
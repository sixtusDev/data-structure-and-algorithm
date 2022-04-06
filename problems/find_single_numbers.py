# In a non-empty array of numbers, every number appears exactly twice except
# two numbers that appear only once. Find the two numbers that appear only once

def find_single_numbers(arr):
    lookup_table = {}

    for i in arr:
        if i in lookup_table:
            lookup_table[i] = lookup_table[i] + 1
        else:
            lookup_table[i] = 1
    
    for i in arr:
        if i in lookup_table:
            if lookup_table[i] == 1:
                continue
            else:
                del lookup_table[i]

    return  list(lookup_table.keys())

def main():
    print(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5]))

main()
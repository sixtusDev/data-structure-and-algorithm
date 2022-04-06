# In a non-empty array of integers, every number appears twice except for one, find that single number

def find_single_number(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result = result ^ arr[i]

    return result

def main():
    print(find_single_number([1, 4, 2, 1, 3, 2, 3]))
    print(find_single_number([7, 9, 7]))

main()
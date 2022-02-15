def search_triplets(array):
    array.sort()
    result = []

    for i in range(len(array)):
        if i > 0 and array[i] == array[i - 1]:
            continue
        low = 0
        high = len(array) - 1
        current_sum = 0 - array[i]

        while low < high:
            if array[low] + array[high] == current_sum:
                result.append([array[i], array[low], array[high]])
                while low < high and  array[low] == array[low + 1]:
                    print("Low")
                    low += 1
                while low < high and  array[high] == array[high - 1]:
                    print("high")
                    high -= 1
                low += 1
                high -= 1
            elif array[low] + array[high] > current_sum:
                high -= 1
            else:
                low += 1
    
    return result

print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
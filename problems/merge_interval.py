def merge_interval(array):
    array.sort(key = lambda i: i[0])
    output = [array[0]]

    for start, end in array[1:]:
        curr_last_item = output[-1][1]

        if start <= curr_last_item:
            print("gggg")
            output[-1][1] = max(end, curr_last_item)
        else:
            output.append([start, end])

    return output

print(merge_interval([[1,4], [2,5], [7,9]]))
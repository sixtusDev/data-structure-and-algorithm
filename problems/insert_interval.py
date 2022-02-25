def insert_interval(intervals, new_interval):
    intervals.append(new_interval)
    intervals.sort(key = lambda i: i[0])

    output = [intervals[0]]

    for start, end in intervals:
        curr_last_item = output[-1][1]

        if curr_last_item >= start:
            output[-1][1] = max(end, curr_last_item)
        else:
            output.append([start, end])

    return output

print(insert_interval([[1,3], [5,7], [8,12]], [4,6]))

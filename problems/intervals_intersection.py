def intervals_intersection(intervals_a, intervals_b):
    output = []
    i = 0
    j = 0

    while i < len(intervals_a) and j < len(intervals_b):
        first_num_a = intervals_a[i][0]
        second_num_a = intervals_a[i][1]
        first_num_b = intervals_b[j][0]
        second_num_b = intervals_b[j][1]

        if first_num_a < first_num_b and second_num_a < second_num_b:
            output.append([max(first_num_a, first_num_b), min(second_num_a, second_num_b)])
            i = i + 1
        elif first_num_a > first_num_b and second_num_a > second_num_b:
            output.append([max(first_num_a, first_num_b), min(second_num_a, second_num_b)])
            j = j + 1
        elif first_num_a == first_num_b and second_num_a == second_num_b:
            output.append([first_num_a, second_num_a])
            i = i + 1
            j = j + 1
        elif first_num_a == second_num_b:
            output.append([first_num_a, first_num_a])
            j = j + 1
        elif second_num_a == first_num_b:
            output.append([second_num_a, second_num_a])
            i = i + 1
        else:
            i = i + 1
            j = j + 1
    
    return output

print(intervals_intersection([[0,2], [5, 10], [13, 23], [24, 25]], [[1,5], [8,12], [15,24], [25,26]]))
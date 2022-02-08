from cgitb import small
import math

def smallest_subarray(array, s):
    window_start = 0
    window_sum = 0
    min_len = math.inf

    for window_end in range(len(array)):
        window_sum += array[window_end]
        
        while window_sum >= s:
            min_len = min(min_len, window_end + 1 - window_start)
            window_sum -= array[window_start]
            window_start += 1

    return min_len

print(smallest_subarray([2,1,5,2,3,2], 7))
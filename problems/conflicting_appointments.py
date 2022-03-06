def conflicting_appointments(intervals):
    intervals.sort()
    
    for i in range(1, len(intervals)):
        print(intervals[i])
        start, end = intervals[i]
        print("Initial", start, end)
        back_start, back_end = intervals[i-1]
        print("Second", back_start, back_end)

        if((back_start < end and back_end > start) or 
            (back_start < end and back_end > start) or 
            (back_start == start and back_end == end) or 
            (back_end == start) or (back_start == end)):
            return False
        
    return True



print(conflicting_appointments([[4,5], [2,3], [3,6]]))
def find_happy_number(num):
    slow, fast = num, num
    
    while True:
        slow = find_squares(slow)
        fast = find_squares(find_squares(fast))
        if slow == fast:
            break
    return slow == 1

def find_squares(num):
    _sum = 0

    while num > 0:
        digit = num % 10
        _sum = _sum + digit * digit
        num //= 10

    return _sum

print(find_happy_number(89))
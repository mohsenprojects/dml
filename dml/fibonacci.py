#-----------------------------------------------------------


def is_fib(num: int) -> bool:
    if num <= 0:
        return False
    if num == 1:
        return True
    
    a, b = 1, 1
    while b < num:
        a, b = b, a + b
    
    return b == num

def nth_fib(n: int) -> int:
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    a, b = 0, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    
    return b

def fib_between(start: int ,lim:int)->list:
    l = []
    for i in range(start, lim):
        if is_fib(i):
            l.append(i)
    return l

def nth_fib_list(start: int, end: int) -> list:
    if start <= 0 or end <= 0 or start > end:
        return []
    
    result = []
    
    if start <= 1 <= end:
        result.append(0)
    if start <= 2 <= end:
        result.append(1)
    if start <= 3 <= end:
        result.append(1)
    
    if end > 3:
        a, b = 1, 1
        for n in range(4, end + 1):
            a, b = b, a + b
            if n >= start:
                result.append(b)
    
    return result
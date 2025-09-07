import dml.log


#--------------------------------------------------------------------------

def is_prime(num: int)->bool:
    if num == 0 : return False
    if num < 0 : return False
    for i in range(1 , int(num**0.5)+1):
        if num % i == 0:
            if i != 1:
                return False
                break
    return True

def next_prime(num: int)->int:
    co = num+1
    while True:
        if is_prime(co):
            return co
            break
        co+=1

def prev_prime(num: int)->int:
    if num <= 2 :
        return None
    else :
        co = num-1
        while True:
            if is_prime(co):
                return co
                break
            co-=1

def prime_factors(num: int)->list:
    factors = []
    i = 2
    while i * i <= num:
        while num % i == 0 :
            factors.append(i)
            num //= i
        i += 1
    if num > 1 :
        factors.append(num)
    return factors


def nth_prime(num: int)->int:
    counter = 2
    counter_num = 0
    while True:
        if (is_prime(counter)):
            counter_num += 1
        if counter_num == num:
            return counter
            break
        counter += 1

def primes_between(start: int , lim: int)->list:
    l = []
    for i in range(start,lim):
        if is_prime(i):
            l.append(i)
    return l

def nth_prime_list(start: int, lim: int)->list:
    l = []
    count_prime = 0
    counter_loop = 1
    while True:
        if is_prime(counter_loop):
            if count_prime >= start:
                l.append(counter_loop)
            count_prime += 1
        counter_loop += 1
        if (count_prime == lim):
            break
    return l

def number_of_primes_between_range(start:int, lim:int)->int:
    if lim <= 1 : return 0
    a = start/dml.ln(start) if start > 1 else 0
    b = lim/dml.ln(lim) if lim > 1 else 0
    if start <= 1:
        return int(b)
    elif start > 1:
        return int(b-a)
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, round(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def minimum_number(num):
    a = 0
    s = sum(num)
    while not isprime(s):
        a += 1
        s += 1
    return a
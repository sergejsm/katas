def is_prime(num):
    if num < 2: return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True



print(is_prime(2))


Shortest solution:

def is_prime(num):
    return num > 1 and not any(num % n == 0 for n in range(2,num))
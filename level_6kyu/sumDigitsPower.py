#First longer solution:

def sum_dig_pow2(a, b): # range(a, b + 1) will be studied by the function
    res = []
    for i in range(a, b+1):
        res2 = 0
        for j,l in enumerate(str(i)):
            res2 += int(l) ** (j+1)
            if res2 == i:
                res.append(res2)
    return res


#Best solution:

def filter_func(a):
    return sum(int(d) ** (i+1) for i, d in enumerate(str(a))) == a

def sum_dig_pow(a, b):
    return filter(filter_func, range(a, b+1))


print(sum_dig_pow(1,150))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
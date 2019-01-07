# My brute solution (doesnt work on big numbers)
def sol_equa2(n):
    res = []
    for x in range(n+1):
        for j in range(n+1):
            if (x - 2*j) * (x + 2*j) == n:
                res.append([x,j])
    return res

# Working Solution:
import math


def sol_equa(n):
    res = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            j = n // i
            if (i + j) % 2 == 0 and (j - i) % 4 == 0:
                x = (i + j) // 2
                y = (j - i) // 4
                res.append([x, y])

    return res
# Hint x2 - 4 * y2 = (x - 2*y) * (x + 2*y)

print(sol_equa(12))  # [[4, 1]])
print(sol_equa(9000))  # [[7, 3]])
# print(sol_equa(16))  # [[4, 0]])
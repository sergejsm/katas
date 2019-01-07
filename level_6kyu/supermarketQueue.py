
#Not my solutions

def queue_time2(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
        print(l)
    return max(l)


def queue_time(customers, n):
    qn = [0] * n
    for c in customers:
        qn = sorted(qn)
        qn[0] += c
    return max(qn)

print(queue_time([5], 2))  # 5
print()
print(queue_time([2,2,3,4,5], 2))  # 16


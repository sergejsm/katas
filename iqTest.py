def iq_test(numbers):
    num_ = list(map(int,numbers.split()))
    even = list(filter(lambda x: x%2 == 0, num_))
    odd = list(filter(lambda x: x%2 != 0, num_))
    if len(even) == 1:
        return num_.index(even[0])+1
    else:
        return num_.index(odd[0])+1

print(iq_test("88 96 66 51 14 88 2 92 18 72 18 88 20 30 4 82 90 100 24 46")) # 4
# print(iq_test("1 2 2")) # 1

Best Solution:
def iq_test2(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1
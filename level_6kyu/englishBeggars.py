def beggars(values, n):
    beggarNumber = 0
    listOfBeggars = [0] * n
    if n == 0:
        return listOfBeggars
    for i in values:
        if beggarNumber >= n : beggarNumber = 0
        listOfBeggars[beggarNumber] += i
        beggarNumber += 1
    return listOfBeggars


#Best Solution:
def beggars2(values, n):
    return [sum(values[i::n]) for i in range(n)]

# print(beggars([1, 2, 3, 4, 5], 1)) #  [15])
print(beggars([1, 2, 3, 4, 5], 2)) #  [9, 6])
# print(beggars([1, 2, 3, 4, 5], 3)) #  [5, 7, 3])
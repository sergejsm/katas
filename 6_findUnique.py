def find_uniq(arr):

    if arr[:3].count(list(set(arr))[0])>1:
        return list(set(arr))[1]
    else:
        return list(set(arr))[0]

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))


#Better Solution:
def find_uniq2(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

def find_uniq3(arr):
    s = set(arr)
    for e in s:
        if arr.count(e) == 1:
            return e
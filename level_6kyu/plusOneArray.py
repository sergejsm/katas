def up_array(arr):
    if not arr:
        return None
    for i in arr:
        if i < 0 or i > 9 :
            return None

    a = int("".join(str(x) for x in arr)) + 1
    return [int(i) for i in list(str(a))]



print(up_array([2, 3, 9]))   # [2, 4, 0]
print(up_array([4, 3, 2, 5]))   # [4, 3, 2, 6]
print(up_array([1, -9]))  # None


#Best Solution:

def up_array2(arr):
  if not arr or min(arr) < 0 or max(arr) > 9:
    return None
  else:
    return [int(y) for y in str(int("".join([str(x) for x in arr])) + 1)]


def up_array3(arr):
    if arr and all(0 <= x <= 9 for x in arr):
        return map(int, str(int(''.join(map(str, arr))) + 1))
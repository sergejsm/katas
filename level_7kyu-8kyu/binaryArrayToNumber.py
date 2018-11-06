
def binary_array_to_number(arr):
    multip = 1
    result = 0
    for i in range(len(arr)-1,-1,-1):
        result += arr[i] * multip
        multip *= 2
    return result



#Best solutions:

def binary_array_to_number2(arr):
    return int("".join(map(str, arr)), 2)

def binary_array_to_number3(arr):
    return int(''.join(str(a) for a in arr), 2)


def binary_array_to_number4(arr):
    s = 0
    for digit in arr:
        s = s * 2 + digit
    return s
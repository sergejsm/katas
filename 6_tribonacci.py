def tribonacci(signature, n):
    result = []
    if n <= 3:
        for i in range(n):
            result.append(signature[i])
    else:
        result = signature
        for i in range(n-3):
            result.append(sum(result[-3:]))

    return result


print(tribonacci([1, 1, 1], 10))



#Best Solution:

def tribonacci2(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res


def tribonacci3(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))

    return signature[:n]
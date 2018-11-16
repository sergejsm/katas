from functools import reduce


def dig_pow(n, p):
    sum = 0
    for i in str(n):
        sum += int(i)**p
        p += 1

    if (sum/n).is_integer():
        return sum/n
    else:
        return -1

#Best Solution:
def dig_pow2(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1

def dig_pow3\
                (n, p):
  t = sum( int(d) ** (p+i) for i, d in enumerate(str(n)))
  return t//n if t%n==0 else -1

print(dig_pow(89, 1))
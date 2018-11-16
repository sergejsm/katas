

#Best solutions:

from itertools import cycle

def make_looper(s):
    g = cycle(s)
    return lambda: next(g)



class make_looper2(cycle):

    def __call__(self):
        return self.__next__()




ar = make_looper("howdy")
print(ar())
print(ar())
print(ar())
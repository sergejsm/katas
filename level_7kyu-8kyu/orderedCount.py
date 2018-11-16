def ordered_count(input):
    results = list()
    tested = list()
    for i in input:
        if i not in tested:
            results.append((i, input.count(i)))
            tested.append(i)
    return results



print(ordered_count('hello'))

#Best Solutions:

from collections import OrderedDict, Counter


class OrderedCounter(Counter, OrderedDict):
    pass


def ordered_count3(seq):
    return list(OrderedCounter(seq).items())


def ordered_count2(_input):
    l = []
    for i in _input:
        if i not in l:
            l.append(i)
    return [(i, _input.count(i)) for i in l]

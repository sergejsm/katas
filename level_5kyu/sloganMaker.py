import itertools

def slogan_maker(array):

    uniqueArray = list()
    for word in array:
        if word not in uniqueArray:
            uniqueArray.append(word)

    tupleList =  list(itertools.permutations(uniqueArray))

    result = list()
    for i in tupleList:
        he = " ".join(i)
        result.append(he)

    return result


print(slogan_maker(['he','ho','he']))


#Best Solution

def slogan_maker(arr):
    return list(map(' '.join, permutations(dict(zip(arr, range(len(arr)))))))

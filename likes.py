def likes(names):
    if names == []:
        return "no one likes this"
    elif len(names) == 1:
        return (str(names[0]) + " likes this")
    else:
        if len(names) == 2:
            return (' and '.join(map(str,names)) + ' like this')

        elif len(names) == 3:
            return (', '.join(map(str, names[:2])) + ' and ' + names[2] + ' like this')

        else:
            return (', '.join(map(str, names[:2])) + ' and ' + str(len(names) - 2) + ' others like this')


#Best Solution:

def likes2(names):
    dict_ = {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this',
    }
    return dict_[min(4, len(names))].format(*names, others = len(names)-2)

def is_isogram(string):
    for i in string:
        if string.lower().count(i) > 1:
            return False
    return True


#Best Solution:

def is_isogram2(string):
    return len(string) == len(set(string.lower()))
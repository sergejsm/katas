def increment_string2(strng):
    strToIncr = get_str_to_incr(strng)
    if strToIncr[0] == False: return strng + '1'
    incr_number = get_incr_numb(strToIncr[0])
    incr_number_str = get_numb_str(incr_number, strToIncr[0])
    return "{}{}".format(strToIncr[1], incr_number_str)

def get_str_to_incr(strn):
    if strn == "" or strn[-1].isdigit() == False: return [False,'']
    i = -1
    while strn[i].isdigit():
        i -= 1
    return [strn[i+1:],strn[0:i+1]]


def get_incr_numb(numb_str):
    numberToIncr = int(numb_str)
    numberToIncr += 1
    return numberToIncr

def get_numb_str(incrementedNumb, stringToVerify):
    if len(str(incrementedNumb)) < len(stringToVerify):
        numbZeroes = len(stringToVerify) - len(str(incrementedNumb))
        return '0'*numbZeroes + str(incrementedNumb)
    return str(incrementedNumb)



# print(increment_string("1")) # Doesnt work
print(increment_string("foo"))
print(increment_string("foo2"))
print(increment_string("foobar009"))



#Best Solution:
def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))
def find_missing_letter(chars):
    letters = ["a","b","c","d","e","f","g","h","i","j","k",
           "l","m","n","o","p","q","r","s","t","u",
           "v","w","x","y","z"]

    first = letters.index(chars[0].lower())
    last = letters.index(chars[-1].lower())

    if chars[0].isupper():
        return (set(letters[first:last+1]) - set([x.lower() for x in chars])).pop().upper()
    else:
        return (set(letters[first:last+1]) - set(chars)).pop()


print(find_missing_letter(['O','Q','R','S']))
print(find_missing_letter(['o','q','r','s']))

#Best Solutions:

def find_missing_letter2(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))

def find_missing_letter3(input):
    alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    start = alphabet.index(input[0])
    for i in range(len(input)):
        if not input[i] == alphabet[start+i]:
            return alphabet[start+i]
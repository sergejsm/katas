def string_transformer(s):
    phrase = list()
    for word in reversed(s.split(" ")):
        changedWord = "".join([l.lower() if l.istitle()  else l.upper() for l in word])
        phrase.append(changedWord)
    return " ".join(phrase)



print(string_transformer("Example string YES"))

#Best Solution:
def string_transformer(s):
    return ' '.join(s.swapcase().split(' ')[::-1])
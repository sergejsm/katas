#First long solution

def duplicate_encode2(word):
    word = word.lower()
    final = []
    for i in word:
        if word.count(i) == 1 :
            final.append('(')
        else:
            final.append(')')
    return ''.join(final)

#Second one-liner (also best solution)
def duplicate_encode(word):
    return ''.join(['(' if word.lower().count(i) == 1 else ')' for i in word.lower()])


print(duplicate_encode("din"))
print(duplicate_encode("recede"))
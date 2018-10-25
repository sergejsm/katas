def getCount(inputStr):
    num_vowels = 0
    for vowel in ['a', 'e', 'i', 'o', 'u' ]:
        num_vowels += inputStr.count(vowel)
    return num_vowels


print(getCount('helloo my dear'))

#Best Solution:
def getCount(s):
    return sum(c in 'aeiou' for c in s)
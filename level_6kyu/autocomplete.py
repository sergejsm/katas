# First Longer Solution:

import re
def autocomplete2(input_, dictionary):
    input_ = re.sub('[^A-Za-z]', '', input_)
    results = list()
    length = len(input_)
    for word in dictionary:
        if word.lower()[:length] == input_:
            results.append(word)

    return results[:5]

# My shorter solution:

def autocomplete(input_, dictionary):
    input_ = re.sub('[^A-Za-z]', '', input_)
    return [word for word in dictionary if word.lower()[:len(input_)] == input_][:5]


dictionary = ['abnormal',
              'arm-wrestling',
              'absolute',
              'Airplane',
              'airport',
              'amazing',
              'apple',
              'ball']


print(autocomplete('!ai', dictionary))   # ['airplane','airport']
print(autocomplete('a', dictionary))  # ['abnormal','arm-wrestling','absolute','airplane','airport']
'''
You need to write regex that will validate a password to make sure it meets the following criteria:

    At least six characters long
    contains a lowercase letter
    contains an uppercase letter
    contains a number

Valid passwords will only be alphanumeric characters.
'''

from re import search

# regex = '[a-zA-Z0-9]{7,}'
regex2 = (r'^(?=.*[a-z])(?=.*\d)(?=.*[A-Z])(?:.{6,})$')


#Solution that works:
regex = (r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$')



print(bool(search(regex, '8lkkqNMMlWo')))
# print(bool(search(regex, 'ghdfj32')))  #False
# print(bool(search(regex, 'DSJKHD23')))  #False
# print(bool(search(regex, 'dsF43')))  #False
# print(bool(search(regex, '4fdg5Fj3')))  #True

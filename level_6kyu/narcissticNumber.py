def narcissistic(value): # First fast attempt
    a = 0
    for i in str(value):
        a += int(i) ** len(str(value))
    return value == a

def narcissistic2(value): # My second try, one liner
    return sum([int(x)**len(str(value)) for x in str(value)]) == value

# Best Solution:
# Using generator comprehension instead of list comprehension
def narcissistic3(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))


print(narcissistic3(371))

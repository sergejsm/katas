# Something goes Here ...

class Fraction:

    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator

    # Equality test

    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num

    def getCommonDenominator(self, other):
        if self.bottom == other.bottom:
            return self.bottom
        elif self.bottom % other.bottom == 0 or other.bottom % self.bottom == 0:
            return max(self.bottom, other.bottom)
        else:
            return self.bottom * other.bottom

    def __add__(self, other):
        denom = self.getCommonDenominator(other)
        return Fraction(denom//self.bottom * self.top +  denom//other.bottom * other.top, denom)

first = Fraction(1,8)
second = Fraction(4,5)

# print(first.getCommonDenominator(second))

print(Fraction(1, 8) + Fraction(4, 5)) # Fraction(37, 40)




"""

class Fraction:

    def __init__(self, numerator, denominator):
        g = gcd(numerator, denominator)
        self.top = numerator / g
        self.bottom = denominator /g
    
    #Equality test
    
    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num
        
    #The rest goes here
    def __add__(self, other):
        numerator = self.top * other.bottom + self.bottom * other.top;
        denominator = self.bottom * other.bottom;
        return Fraction(numerator, denominator)
    
    def __str__(self):
        return str(self.top) + "/" + str(self.bottom)

def gcd(x, y):
    if (y == 0):
        return x
    return gcd(y, x % y)
"""
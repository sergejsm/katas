import math
class Vector:
    def __init__(self, dims):
        self.dims = dims

    def add(self, other):
        if len(self.dims) != len(other.dims):
            raise Exception
        return [self.dims[i] + other.dims[i] for i in range(len(self.dims))]

    def substract(self, other):
        if len(self.dims) != len(other.dims):
            raise Exception
        return [self.dims[i] - other.dims[i] for i in range(len(self.dims))]

    def dot(self, other):
        if len(self.dims) != len(other.dims):
            raise Exception
        return sum([self.dims[i] * other.dims[i] for i in range(len(self.dims))])

    def equals(self, other):
        if len(self.dims) != len(other.dims):
            raise Exception
        if False in [self.dims[i] == other.dims[i] for i in range(len(self.dims))]:
            return False
        else:
            return True

    def norm(self):
        return math.sqrt(sum(x**2 for x in self.dims))

    def toString(self):
        return str(tuple(self.dims))



a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])
d = Vector([1, 2, 3])

print(a.add(b))
print(a.substract(b))
print(a.dot(b))
print(a.norm())
print(a.toString())
print(a.equals(d))

# print(a.add(c))

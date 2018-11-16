class Package2(object):
    def __init__(self, length, width, height, weight):
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight

        self.checkValues()

    @property
    def volume(self):
        return self.length * self.width * self.height

    def checkValues(self):
        if 0 > self.length:
            print('hoo')
            raise DimensionsOutOfBoundError(f"Package {variable}=={value} out of bounds, should be: {lower} < {variable} <={upper}")
        if 0 >= self.width > 300:
            raise DimensionsOutOfBoundError()
        if 0 >= self.height > 150:
            raise DimensionsOutOfBoundError()
        if 0 >= self.weight > 40:
            raise DimensionsOutOfBoundError()

        # f"Package {variable}=={value} out of bounds, should be: {lower} < {variable} <={upper}"


class DimensionsOutOfBoundError2(Exception):
    def __init__(self, l):
        Exception.__init__(self, f"well, that {l}")



#Best solution:

class Package(object):
    maxs = {"length": 350, "width": 300, "height": 150, "weight": 40}

    def __init__(self, l, w, h, wg):
        self.length = l
        self.width = w
        self.height = h
        self.weight = wg

    def __setattr__(self, att, v):
        if v <= 0 or v > Package.maxs[att]: raise DimensionsOutOfBoundError(att, v, Package.maxs[att])
        self.__dict__[att] = v

    @property
    def volume(self):
        return self.length * self.width * self.height


class DimensionsOutOfBoundError(Exception):
    def __init__(self, dim, val, max):
        self.str = "Package %s==%d out of bounds, should be: 0 < %s <= %d" % (dim, val, dim, max)

    def __str__(self):
        return self.str



l = Package(-1, 0.2, 0.2, 0.2)
print(l.volume)
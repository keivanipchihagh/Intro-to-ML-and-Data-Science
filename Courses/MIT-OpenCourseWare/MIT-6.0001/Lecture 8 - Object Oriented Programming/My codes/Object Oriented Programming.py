class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5


c = Coordinate(3,4)
origin = Coordinate(0,0)
print(c.distance(origin))
print(Coordinate.distance(c, origin))
print(origin.distance(c))

class Fraction(object):
    def __init__(self, num, denom):
        assert type(num) == int and type(denom) == int,
        self.num = num
        self.denom = denom
    def __str__(self):
        return str(self.num) + "/" + str(self.denom)
    def __add__(self, other):
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __sub__(self, other):
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __float__(self):
        return self.num/self.denom
    def inverse(self):
        return Fraction(self.denom, self.num)

a = Fraction(1,4)
b = Fraction(3,4)
c = a + b
print(Fraction.__float__(c))
print(float(b.inverse()))

#c = Fraction(3.14, 2.7) # assertion error
#print a*b # error, did not define how to multiply two Fraction objects

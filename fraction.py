__author__ = 'Steven Sarasin'


def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


class Fraction:
    def __init__(self, top, bottom=1):
        if bottom < 0:
            top = -top
            bottom = -bottom

        if type(top) == float or type(bottom) == float:
            from math import floor
            top_top = top
            top_bottom = 1
            bottom_top = bottom
            bottom_bottom = 1
            while floor(top_top) < top_top:
                top_top *= 10
                top_bottom *= 10
            while floor(bottom_top) < bottom_top:
                bottom_top *= 10
                bottom_bottom *= 10
            top = int(top_top * bottom_bottom)
            bottom = int(bottom_top * top_bottom)

        if top == 0:
            self.num = 0
            self.den = 1
        else:
            self.num = top / gcd(abs(top), bottom)
            self.den = bottom / gcd(abs(top), bottom)

    def __add__(self, other):
        if type(other) != type(self):
            other = Fraction(other)
        top = self.num * other.den + other.num * self.den
        bottom = self.den * other.den
        return Fraction(top, bottom)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if type(other) != type(self):
            other = Fraction(other)
        return Fraction(self.num * other.num, self.den * other.den)

    def __div__(self, other):
        if type(other) != type(self):
            other = Fraction(other)
        return Fraction(self.num * other.den, self.den * other.num)

    def __truediv__(self, other):
        return Fraction(self.num * other.den, self.den * other.num)

    def __radd__(self, other):
        return Fraction(other).__add__(self)
    
    def __rsub__(self, other):
        return Fraction(other).__sub__(self)
    
    def __rmul__(self, other):
        return Fraction(other).__mul__(self)
    
    def __rdiv__(self, other):
        return Fraction(other).__div__(self)

    def __rtruediv__(self, other):
        return Fraction(other).__truediv__(self)

    def __neg__(self):
        return Fraction(-self.num, self.den)

    def __str__(self):
        if self.num == 0:
            return str(0)
        if self.den == 1:
            return str(self.num)
        else:
            return str(self.num) + "/" + str(self.den)

    def tex_frac(self):
        return "\\frac{" + str(self.num) + "}{" + str(self.den) + "}"

    def __eq__(self, other):
        return float(self) == float(other)

    def __lt__(self, other):
        return float(self) < float(other)

    def __gt__(self, other):
        return not (self < other)

    def __float__(self):
        return float(self.num) / float(self.den)

    def __int__(self):
        return self.num / self.den

if __name__ == "__main__":

    my_frac = Fraction(3, 5)
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    print Fraction(1, 2) * my_frac
    f3 = f1 + f2
    print f3
    print Fraction(3, 3)
    print Fraction(2, 4) == Fraction(1, 2)
    print Fraction(1, 3) - Fraction(12, 24)

    print f1, " > ", f2, f1 > f2
    print f1, " < ", f2, f1 < f2
    print f1, " == ", f2, f1 == f2
    print Fraction(1.3, -2.1)
    print Fraction(1.3 / 2.1)
    f = Fraction(3.2)
    print f, "=", float(f), "about =", int(f)

    print "\\frac{1}{3} * 3 = ", Fraction(1, 3) * 3
    print "3 * \\frac{1}{3} = ", 3 * Fraction(1, 3)
    print "\\frac{1}{3} * 3 = ", Fraction(1, 3) * 3
    print "3 / \\frac{1}{2} = ", 3 / Fraction(1, 2)
    print "\\frac{1}{3} / 3 = ", Fraction(1, 3) / 3
    print "3 - \\frac{1}{3} = ", 3 - Fraction(1, 3)
    print "\\frac{1}{3} - 3 = ", Fraction(1, 3) - 3
    print "3 + \\frac{1}{3} = ", 3 + Fraction(1, 3)
    print "\\frac{1}{3} + 3 = ", Fraction(1, 3) + 3
    print "-\\frac{3}{1} = ", -Fraction(3, 1)
    print "\\frac{1}{3} - \\frac{1}{3} = ", Fraction(1, 3)-Fraction(1, 3)
    print "\\frac{1}{3} + \\frac{1}{3} = ", Fraction(1, 3) + Fraction(1, 3)
    print "\\frac{1}{3} + 1 = ", Fraction(1, 3) + 1
    print "\\frac{3}{1} + \\frac{1}{3} = ", Fraction(3, 1) + Fraction(1, 3)
    print "\\frac{1}{2} - \\frac{1}{3} = ", Fraction(3, 2) - Fraction(1, 3)
    print "\\frac{3}{1} - \\frac{1}{3} = ", Fraction(3, 1) + Fraction(1, 2)
    print "\\frac{2}{1} - \\frac{1}{2} = ", Fraction(3, 1) - Fraction(1, 2)
    print "-\\frac{1}{3} = ", -Fraction(1, 3)
    print "\\frac{3}{1} = ", Fraction(3, 1)
    print "\\frac{4}{1} - \\frac{1}{3} = ", Fraction(4, 1) - Fraction(1, 3)
    print "3 > frac(2,1) is ", 3 > Fraction(2, 1)
    print Fraction(2, 1).tex_frac()
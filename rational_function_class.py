# Represents a rational number P(x)/Q(x)

class RationalFunction:
    def __init__(self, a, b):
        self.a, self.b = a, b
    
    def __str__(self):
        return "(" + str(self.a) + ")/(" + str(self.b) + ")"
     
    def __repr__(self):
        return "(" + str(self.a) + ")/(" + str(self.b) + ")"
    
    def __add__(self, other):
        newA = self.a * other.b + other.a * self.b
        newB = self.b * other.b 
        return RationalFunction(newA, newB)
    
    def __mul__(self, other):
        return RationalFunction(self.a * other.a, self.b * other.b)
    
    def __sub__(self, other):
        return self + other * (-1)

    def __pow__(self, k):
        return RationalFunction(self.a**k, self.b**k)

# # Turns a real number into a rational number
# def coerceRational(num):
#     if isinstance(num, float) or isinstance(num, int):
#         return Rational(num, 1)
#     else:
#         return num  
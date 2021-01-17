import random

class Polynomial:
    # Polynomial can be represented as an array of coefficients. 
    # For example, 4x^4 + 2x^2 + 4x - 5 would be represented as Polynomial([4,0,2,4,-5])

    def __init__(self, coef):
        self.coef = removeFrontZeroes(coef)
        self.degree = len(self.coef) - 1
    
    def __repr__(self):
        # Returns a string representing a polynomial, in decreasing order of powers
        s = ""
        if self.coef == [0]:
            return "0"
        for i, c in enumerate(self.coef):
            power = self.degree - i
            s += showCoef(c, power)
        if s[:3] == " + ": # remove leading plus signs
            return s[3:]
        else:
            return s[1:]

    def __add__(self, other):
        # Addition of polynomials
        return Polynomial(addArrays([self.coef, other.coef]))

    def scale(self, k):
        # Scale a polynomial by a number k
        return Polynomial([k * a for a in self.coef])

    def __sub__(self, other):
        # Subtraction of polynomials
        return self + other.scale(-1)

    def __mul__(self, other):
        # Multiplication of polynomials
        ps = []
        for i, c in enumerate(self.coef):
            deg = self.degree - i
            shiftedArray = other.coef  + [0] * deg # By adding zeroes to the end of the array, we are shifting by the degree we are multiplying by
            ps.append([c * elem for elem in shiftedArray]) # Then we scale by the value we are multiplying by
        return Polynomial(addArrays(ps))

    def __pow__(self, k):
        # Raises a polynomial to a non negative integer power
        if k >= 0 and isinstance(k, int):
            if k == 0:
                return Polynomial([1])
            else:
                p = self
                for i in range(k-1):
                    p = p * p
                return p
        else:
            print("Must raise polynomial to non-negative integer power in order to be polynomial")
            return None

    def eval(self, x):
        # Evaluates a polynomial for a given number x
        return sum([c*x**(self.degree - i) for i, c in enumerate(self.coef)])

    def compose(self, other):
        # Composition of two polynomials, self(other)
        ps = []
        for i, c in enumerate(self.coef):
            deg = self.degree - i
            ps.append((other**deg).scale(c).coef) # Substitute polynomial into each term, raise to power, scale by coefficient and then add the coefficients array
        return Polynomial(addArrays(ps))

    def derivative(self, n=1):
        # Differentiates a polynomial n times. 
        if n == 0:
            return self
        else:
            deriv = Polynomial([(self.degree - i) * c for i, c in enumerate(self.coef[:-1])]) if self.coef != [0] else Polynomial([0])
        return deriv.derivative(n-1)

    def newton(self, iterations = 10, r = 10, tolerance = 0.01):
        # Gives a root for a polynomial, using Newton's method of approximation
        # iterations is the number of times we apply the algorithm. r is the range in which we randomly choose a root, tolerance is how precise do we need the approximation for it to be a root
        x = random.random() * r * 2 - r//2
        deriv = self.derivative()
        for i in range(iterations):
            f, fprime = self.eval(x), deriv.eval(x)
            x = x - f / fprime
        if abs(self.eval(x)) < tolerance:
            return x
        else:
            print("No root found")
            return None

    def copyP(self):
        return Polynomial(self.coef)


## Helper functions

def removeFrontZeroes(arr):
    # Given an array with a number of zeroes at the front, remove all front zeroes. 
    allZeroes = lambda arr : arr == [0] * len(arr) 
    if allZeroes(arr):
        return [0]
    i = 1
    while allZeroes(arr[:i]):
        i += 1
    return arr[i-1:]

def showCoef(val, deg):
    # Helper function for printing polynomials. Since notation is weird, there's many if else statements
    if val == 0:
        return ""
    else:    
        if deg == 0:
            return " + " + str(val) if val > 0 else " - " + str(abs(val)) 
        elif deg == 1:
            if val == 1 or val == -1:
                return " + X" if val == 1 else " - X"
            else:
                return " + " + str(val) + "X" if val > 0 else " - " + str(-val) + "X"
        else:
            if val == 1 or val == -1:
                return " + X^" + str(deg) if val == 1 else " - X^" + str(deg)
            else:
                return " + " + str(val)+  "X^" + str(deg) if val > 0 else " - " + str(-val) + "X^" + str(deg)

def elongate(arr, length):
    # Elongates an array by adding zeroes to the front
    if len(arr) < length:
        return [0] * (length - len(arr)) + arr  
    else:
        return arr

def addArrays(arrs):
    # Brings all arrays to the same length by adding zeroes to the front, then adds them up element-wise
    maxLength = max([len(arr) for arr in arrs])
    normalisedArrs = [elongate(arr, maxLength) for arr in arrs]
    final = [0] * maxLength # This holds the sum of each index.
    addArr = lambda arr1, arr2 : [a + b for a,b in zip(arr1, arr2)] 
    for arr in normalisedArrs:
        final = addArr(final, arr)
    return final

## Example polynomials

p = Polynomial([3,4,5])
q = Polynomial([-1, 2])
r = Polynomial([-2, 0, 3])

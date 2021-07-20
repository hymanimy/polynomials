# Divides polynomials and returns a quotient polynomial and remainder rational function 
from polynomial_class import *
from rational_function_class import *

def divide(p, q):
    # Algebraic division algorithm
    num, den = p.copyP(), q.copyP()
    quotient = [] # Quotient will by a polynomial 
    for i in range(0, den.degree + 1):
        term = num.coef[0] / den.coef[0]
        power = num.degree - i - den.degree
        poly = Polynomial([term] + [0]*power)
        quotient.append(term)
        num = num - den * poly
    return Polynomial(quotient), RationalFunction(num, den)

def printResult(p, q):
    quotient, remainder = divide(p, q)
    print(f"{p} DIVIDED BY {q} EQUALS {quotient} PLUS {remainder}")
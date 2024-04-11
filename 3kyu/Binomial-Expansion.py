# DESCRIPTION:
# The purpose of this kata is to write a program that can do some algebra.

# Write a function expand that takes in an expression with a single, one character variable, and expands it. 
# The expression is in the form (ax+b)^n where a and b are integers which may be positive or negative, x is any single character variable, and n is a natural number. 
# If a = 1, no coefficient will be placed in front of the variable. If a = -1, a "-" will be placed in front of the variable.

# The expanded form should be returned as a string in the form ax^b+cx^d+ex^f... where a, c, and e are the coefficients of the term, x is the original one character variable that was passed in the original expression and b, d, and f, are the powers that x is being raised to in each term and are in decreasing order.

# If the coefficient of a term is zero, the term should not be included. 
# If the coefficient of a term is one, the coefficient should not be included. 
# If the coefficient of a term is -1, only the "-" should be included. If the power of the term is 0, only the coefficient should be included. 
# If the power of the term is 1, the caret and power should be excluded.

# My solution

import math

def axb_extract(expr):
    expr = expr[::-1]
    parts = expr.split('+', 1)
    if len(parts) != 2:
        parts = expr.split('-', 1)
        parts[0] += '-'

    a_str = parts[1]
    a_str = a_str[1:]
    a_str = a_str[::-1]
    if a_str == '' or a_str == '-':
        a_str += '1'

    a = int(a_str)
    x = parts[1][0]
    b = int(parts[0][::-1])

    return a, x, b

def binom_coef(n):
    top = list(range(n, math.floor((n+1)/2), -1))
    bot = list(range(1, math.ceil((n+1)/2), 1))

    for i in range(1, len(top)):
        top[i] *= top[i-1]
        bot[i] *= bot[i-1]

    coef = [1]
    for i in range(len(top)):
        coef.append(top[i]//bot[i])

    coef2 = coef if n % 2 == 1 else coef[:-1]
    coef += coef2[::-1]

    return coef

def expand(expr):
    parts = expr.split('^', 1)
    exponent = int(parts[1])

    if exponent == 0:
        return '1'
    elif exponent == 1:
        return parts[0][1:-1]

    a, x, b = axb_extract(parts[0][1:-1])

    coef = binom_coef(exponent)
    # print(bc)

    qa = 1
    qb = 1
    for i in range(exponent+1):
        coef[exponent-i] *= qb
        coef[i] *= qa
        qb *= b
        qa *= a

    elements = []

    for i in range(exponent, -1, -1):
        sign = '+' if coef[i] > 0 else '-'
        elem_coef = abs(coef[i]) if abs(coef[i]) > 1 else ''
        if i > 1:
            elements.append('{}{}{}^{}'.format(sign, elem_coef, x, i))
        elif i == 1:
            elements.append('{}{}{}'.format(sign, elem_coef, x))
        else:
            elements.append('{}{}'.format(sign, elem_coef))

    if elements[0][0] == '+':
        elements[0] = elements[0][1:]

    if len(elements[-1]) == 1:
        elements[-1] += '1'

    return ''.join(elements)

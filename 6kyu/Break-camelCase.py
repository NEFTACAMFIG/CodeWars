# DESCRIPTION:

# Complete the solution so that the function will break up camel casing, using a space between words.

# Example

# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

# MY SOLUTION

def solution(s):
    x = 0
    y = []
    for i in s:
        if i == s[x].upper():
            y.append(' ')
            y.append(i)
            x = x + 1
        else:
            y.append(i)
            x = x + 1
    return "".join(y)

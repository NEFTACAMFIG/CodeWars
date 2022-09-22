#DESCRIPTION:

#Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

#Examples input/output:

#XO("ooxx") => true
#XO("xooxx") => false
#XO("ooxXm") => true
#XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
#XO("zzoo") => false

#MY SOLUTION

def xo(s):
    y = ''
    for i in s:
        y = y + i.lower()

    return True if y.count('x') == y.count('o') or (y.count('x')==0 and y.count('o')==0) else False

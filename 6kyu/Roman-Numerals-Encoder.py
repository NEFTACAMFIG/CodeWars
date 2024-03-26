#DESCRIPTION:

#Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

#Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

#Example:

#solution(1000) # should return 'M'

#Help:

#Symbol    Value
#I          1
#V          5
#X          10
#L          50
#C          100
#D          500
#M          1,000

#Remember that there can't be more than 3 identical symbols in a row.

#More about roman numerals - http://en.wikipedia.org/wiki/Roman_numerals

#MY SOLUTION

roman = {
    1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX',  
    10:'X', 20:'XX', 30:'XXX', 40:'XL', 50:'L', 60:'LX', 70:'LXX', 80:'LXXX', 90:'XC', 
    100:'C', 200:'CC', 300:'CCC', 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC', 900:'CM',
    1000:'M', 2000:'MM', 3000:'MMM'
}
def solution(n):
    x = len(str(n)) - 1
    y = []
    w = []
    for i in str(n):
        i = int(i) * pow(10,x)
        x = x - 1
        y.append(i)

    for k in y:
        for j in roman:
            if k == j:
                w.append(roman[j])
    return ''.join(w)

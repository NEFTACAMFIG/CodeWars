# DESCRIPTION:
# Create a function that takes a Number as its argument and returns a Chinese numeral string. You don't need to validate the input argument, it will always be a Number in the range [-99999.999, 99999.999], rounded to 8 decimal places.

# Simplified Chinese numerals have characters representing each number from 0 to 9 and additional numbers representing larger numbers like 10, 100, 1000, and 10000.

# My Solution

def to_chinese_numeral(n):
    numerals = {"-":"负", ".":"点",
                0:"零", 1:"一", 2:"二", 3:"三", 4:"四", 5:"五", 6:"六", 7:"七", 8:"八", 9:"九", 10:"十",
                100:"百", 1000:"千", 10000:"万"}

    a = str(abs(n))
    y = []
    w = []
    z = []
    p = []
    t = []

    if n in numerals and n < 11:
        return numerals[n]

    elif abs(n) in numerals and abs(n) < 11:
        return numerals['-'] + numerals[abs(n)]
    
    elif n >= 11 and n < 20:
        return numerals[10] + numerals[int(a[-1])]

    elif n > -20 and n <= -11:
        return numerals['-'] + numerals[10] + numerals[int(a[-1])]
    
    
    if '.' not in a:
        b = a[0:-1]
        x = len(a) - 1

    elif '.' in a:
        c = a.split('.')
        b = c[0][0:-1]
        x = len(c[0]) - 1
        if len(c[0]) == 1 and c[0] == '0':
            for i in c[1]:
                i = int(i)
                for j in numerals:
                    if i == j:
                        t.append(numerals[i])
            s = ''.join(t)

            if str(n)[0] != '-':
                return numerals[0] + numerals['.'] + s
            else:
                return numerals['-'] + numerals[0] + numerals['.'] + s        
    
        elif c[0] == '10':
            for i in c[1]:
                i = int(i)
                for j in numerals:
                    if i == j:
                        t.append(numerals[i])
            s = ''.join(t)

            if str(n)[0] != '-':
                return numerals[10] + numerals['.'] + s
            else:
                return numerals['-'] + numerals[10] + numerals['.'] + s 
        
    for i in b:
        if int(i) != 0:
            i = (int(i)/int(i)) * pow(10,x)
            x = x - 1
            y.append(i)
        else:
            x = x - 1

    for i in b:
        i = int(i)
        for j in numerals:
            if i == j:
                z.append(numerals[i])

    for k in y:
        for j in numerals:
            if k == j:
                w.append(numerals[j])

    while "零" in z:
        z.remove("零")

    o = 0
    for i, j in enumerate(b):
        if j  == '0' and a[i+1] != '0': 
            p.append(numerals[0])
        elif j  == '0' and a[i+1] == '0': 
            o = o
        else: 
            p.append(z[o])
            p.append(w[o]) 
            o = o + 1

    if '.' not in a:
        if a[-1] != '0':
            p.append(numerals[int(a[-1])])
            if str(n)[0] == '-':
                p = [numerals['-']] + p
        elif a[-1] == '0':
            if str(n)[0] == '-':
                p = [numerals['-']] + p

        return ''.join(p)
    
    elif '.' in a:
        if c[0][-1] != '0':
            p.append(numerals[int(c[0][-1])])
            for i in c[1]:
                i = int(i)
                for j in numerals:
                    if i == j:
                        t.append(numerals[i])
            s = ''.join(t)
            
        elif c[0][-1] == '0':
            for i in c[1]:
                i = int(i)
                for j in numerals:
                    if i == j:
                        t.append(numerals[i])
            s = ''.join(t)


        if str(n)[0] != '-':
            return ''.join(p) + numerals['.'] + s
        else:
            return numerals['-'] + ''.join(p) + numerals['.'] + s

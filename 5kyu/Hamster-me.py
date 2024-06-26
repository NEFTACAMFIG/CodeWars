# Task
# Write a function that accepts two inputs: code and message and returns an encrypted string from message using the code.
# The code is a string that generates the key in the way shown below:

 # 1  | h a m s t e r
 # 2  | i b n   u f
 # 3  | j c o   v g
 # 4  | k d p   w
 # 5  | l   q   x
 # 6  |         y
 # 7  |         z
# All letters from code get number 1. All letters which directly follow letters from code get number 2 (unless they already have a smaller number assigned), etc. It's difficult to describe but it should be easy to understand from the example below:

 # 1  | a e h m r s t
 # 2  | b f i n     u
 # 3  | c g j o     v
 # 4  | d   k p     w
 # 5  |     l q     x
 # 6  |             y
 # 7  |             z
# How does the encoding work using the hamster code?

# a => a1
# b => a2
# c => a3
# d => a4
# e => e1
# f => e2
# ...
# And applying it to strings :

# hamsterMe('hamster', 'hamster')   => h1a1m1s1t1e1r1
# hamsterMe('hamster', 'helpme')    => h1e1h5m4m1e1
# And you probably started wondering what will happen if there is no a in the code.
# Just add these letters after the last available letter (in alphabetic order) in the code.

# The key for code hmster is:

 # 1  | e h m r s t
 # 2  | f i n     u
 # 3  | g j o     v
 # 4  |   k p     w
 # 5  |   l q     x
 # 6  |           y
 # 7  |           z
 # 8  |           a
 # 9  |           b
# 10  |           c
# 11  |           d

# Additional notes
# The code will have at least 1 letter.
# Duplication of letters in code is possible and should be handled.
# The code and message consist of only lowercase letters.

# MY SOLUTION

import string
def hamster_me(code, message):
    abd = {}
    num = {}
    z = []
    w = []
    s = []
    f = 0
    y = sorted(code)
    g = list(string.ascii_lowercase)

    for i in g:
        abd[i] = f
        num[f] = i
        f = f + 1

    for i,x in enumerate(y[:-1]):
        w.append([abd[y[i]],abd[y[i+1]]])

    for i in w:
        r = []
        for j in range(i[0],i[-1]):
            r.append(num[j])
        s.append(r)

    p2 = []
    if y[0] == 'a':
        p = [num[i] for i in range(abd[y[-1]],26)]
    
    else:
        p = [num[i] for i in range(abd[y[-1]],26)]
        p1 = [num[i] for i in range(0,abd[y[0]])]
        p2 = p + p1

    if y[0] == 'a':
        s.append(p)
    else:
        s.append(p2)
        
    s1 = sum(s,[])

    h = []
    anew = {}
    for i in s:
        e =[]
        for j in range(len(i)):
            e.append(i[0]+str(j+1))
        h = h + e

    for i in range(len(h)):
        anew[num[abd[s1[i]]]] = h[i]
        
    r = ''
    for i in message:
        r = r + anew[i]

    return r

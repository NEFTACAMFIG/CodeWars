# DESCRIPTION:
# Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

# s1 = "A aaaa bb c"

# s2 = "& aaa bbb c d"

# s1 has 4 'a', 2 'b', 1 'c'

# s2 has 3 'a', 3 'b', 1 'c', 1 'd'

# So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. 
# In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.

# We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.

# The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

# In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits - more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".

# Hopefully other examples can make this clearer.

# s1 = "my&friend&Paul has heavy hats! &"
# s2 = "my friend John has many many friends &"
# mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

# s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
# s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
# mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

# s1="Are the kids at home? aaaaa fffff"
# s2="Yes they are here! aaaaa fffff"
# mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
# Note for Swift, R, PowerShell
# The prefix =: is replaced by E:

# s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
# s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
# mix(s1, s2) --> "1:mmmmmm/E:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/E:ee/E:ss"

My Solution

import string
def mix(s1, s2):
    yo1 = []
    yo2 = [] 
    yo = ''
    s1 = s1.split()
    s2 = s2.split()
    ro = []
    
    s11 = {}
    s22 = {}
    fin = {}
    
    for i in s1:
        for j in i:
            if j.islower():
                s11[j]=[]

    for i in s1:
        for j in i:
            if j.islower():
                s11[j].append(j)
            
    for i in s2:
        for j in i:
            if j.islower():
                s22[j]=[]

    for i in s2:
        for j in i:
            if j.islower():
                s22[j].append(j)
            
    for i in s11.keys():
        if i in s22.keys():
            if len(s11[i]) >= len(s22[i]) and len(s11[i]) > 1:
                fin['1'+i] = s11[i]
            elif len(s11[i]) < len(s22[i]) and len(s22[i]) > 1:
                fin['2'+i] = s22[i]
        elif i not in s22.keys() and len(s11[i]) > 1:
            fin['1'+i] = s11[i]

    for i in s22.keys():
        if i not in s11.keys() and len(s22[i]) > 1:
            fin[i] = s22[i]
            
    ho = [fin[k][0] for k in sorted(fin, key=lambda k:len(fin[k]),reverse=True)]
    
    for i in ho:
        if i in s11.keys() and i in s22.keys():
            if len(s11[i]) > len(s22[i]) and len(s11[i]) > 1:
                s11[i].insert(0,3)
                ro.append(s11[i])
            elif len(s11[i]) < len(s22[i]) and len(s22[i]) > 1:
                s22[i].insert(0,2)
                ro.append(s22[i])
            elif len(s11[i]) == len(s22[i]) and len(s22[i]) > 1 and len(s11[i]) > 1:
                s11[i].insert(0,1)
                ro.append(s11[i])
        elif i in s11.keys() and i not in s22.keys() and len(s11[i]) > 1:
            s11[i].insert(0,3)
            ro.append(s11[i])
        elif i not in s11.keys() and i in s22.keys() and len(s22[i]) > 1:
            s22[i].insert(0,2)
            ro.append(s22[i])

    ro = sorted(ro, key = lambda l: (len(l),l[0],26 - string.ascii_lowercase.index(l[1].lower())),reverse = True)
    
    if ro == []:
        return ''
    else:
        for i in ro:
            if i[0] == 3:
                i[0] = 1
                yo = yo + str(i[0])+':'+''.join(i[1:])+'/'
            elif i[0] == 1:
                i[0] = '='
                yo = yo + str(i[0])+':'+''.join(i[1:])+'/'
            else:
                yo = yo + str(i[0])+':'+''.join(i[1:])+'/'
        return yo[0:-1]

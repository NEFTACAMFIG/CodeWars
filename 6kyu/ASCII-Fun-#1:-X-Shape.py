# DESCRIPTION:
# You will get an odd integer n (>= 3) and your task is to draw an X. Each line is separated with \n.

# Use the following characters: ■ □ For Ruby, Crystal and PHP: whitespace and o

# Examples

  #                                    ■□□□■
    #         ■□■                      □■□■□
  # x(3) =>   □■□             x(5) =>  □□■□□
    #         ■□■                      □■□■□
       #                               ■□□□■


# MY SOLUTION

def x(n):
    t = '■' + '□'*(n-2) + '■'
    f = ''
    g = ''
    g_1 = ''
    j = (n-4)
    y = 1

    for i in range(int((n-3)/2)):
        g = g + '□'*(i+1) +'■' + '□'*(j) + '■' + '□'*(i+1) + '\n'
        j = j - 2

    for i in reversed(range(int((n-3)/2))):
        g_1 = g_1 + '□'*(i+1) +'■' + '□'*(y) + '■' + '□'*(i+1) + '\n'
        y = y + 2

    for i in range(5):
        if i == 0 or i == 4:
            f = f + t +'\n'
        elif i == 2:
            f = f + '□'*int((n-1)/2) + '■' + '□'*int((n-1)/2) + '\n'
        elif i == 1:
            f = f + g
        else:
            f = f + g_1
            
    return f[:-1]

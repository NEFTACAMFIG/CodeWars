# DESCRIPTION:
# Funny Dots
# You will get two integers n (width) and m (height) and your task is to draw the following pattern. Each line is seperated with a newline (\n)

# Both integers are equal or greater than 1; no need to check for invalid parameters.

# Examples

  #                                          +---+---+---+
   #          +---+                          | o | o | o |
#dot(1, 1) => | o |            dot(3, 2) =>  +---+---+---+            
  #           +---+                          | o | o | o |
   #                                         +---+---+---+



#MY SOLUTION

def dot(n,m):
    s = ''
    g = ''
    t = ''
    y = '+---+\n| o |\n+---+'
    a = '+---'
    b = '| o '

    if n == 1 and m == 1:
        return y
    
    else:
        s = s + a*n + '+' + '\n' + b*n + '|' + '\n'
        g = g + a*n 
        for i in range(m):
            t = t + s
    t = t + g + '+'  
    return t

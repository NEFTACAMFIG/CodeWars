# DESCRIPTION:

# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

# MY SOLUTION

def move_zeros(lst):
    y = []
    x = 0
    for i in lst:
        if i == 0:
            x = x + 1
        else:
            y.append(i)
    for j in range(x):
        y.append(0)
    return y

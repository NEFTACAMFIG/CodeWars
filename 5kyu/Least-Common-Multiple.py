# DESCRIPTION:
# Write a function that calculates the least common multiple of its arguments; each argument is assumed to be a non-negative integer. 
# In the case that there are no arguments (or the provided array in compiled languages is empty), return 1. If any argument is 0, return 0.

# MY SOLUTION

import numpy as np
def lcm(*args):
    if args ==():
        return 1
    else:
        y = [i for i in args]
        arr = np.array(y)
        return np.lcm.reduce(arr)

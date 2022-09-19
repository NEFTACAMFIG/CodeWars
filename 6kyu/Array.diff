#DESCRIPTION:

#Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

#It should remove all values from list a, which are present in list b keeping their order.

#array_diff([1,2],[1]) == [2]

#If a value is present in b, all of its occurrences must be removed from the other:

#array_diff([1,2,2,2,3],[2]) == [1,3]

#MY SOLUTION

def array_diff(a, b):
    y = []
    for i in a:
        for j in list(set(b)):
            if i==j:
                y.append(i)

    for k in y:
        a.remove(k)
    return a

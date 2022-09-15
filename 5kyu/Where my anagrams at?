#DESCRIPTION:

#What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

#'abba' & 'baab' == true

#'abba' & 'bbaa' == true

#'abba' & 'abbba' == false

#'abba' & 'abca' == false

#Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

#anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

#anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

#anagrams('laser', ['lazing', 'lazy',  'lacer']) => []


#MY SOLUTION

def anagrams(word, words):
    y = []
    for i in words:
        if len(word) == len(i):
            if sorted(list(set(word))) == sorted(list(set(i))):
                y.append(i)

    return y
  

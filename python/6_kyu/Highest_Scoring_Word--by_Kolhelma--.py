#2021-09-21 12:57:34.204000+00:00
"""Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: `a = 1, b = 2, c = 3` etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid."""

def high(x):
    x = x.split()
    sums = []
    for i in x:
        s = 0
        for l in i:
            s += ord(l) - 96
        sums.append(s)
    return (x[sums.index(max(sums))])
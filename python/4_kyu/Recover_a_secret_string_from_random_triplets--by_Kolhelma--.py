#2021-10-10 16:18:35.617000+00:00
"""There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string. 

A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the secret string.

You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string. In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you."""

from itertools import chain

def index_check(l, i1, i2):
    if l.index(i1) > l.index(i2):
        l.remove(i1), l.insert(l.index(i2), i1)

def recoverSecret(triplets):
    lett = list(set(chain(*triplets)))
    for i in triplets:
        index_check(lett, i[1], i[2])
        index_check(lett, i[0], i[1])
    return "".join(lett)
        
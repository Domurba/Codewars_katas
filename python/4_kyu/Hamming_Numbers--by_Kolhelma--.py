#2021-09-08 12:19:09.657000+00:00
"""A *[Hamming number][1]* is a positive integer of the form 2<sup>*i*</sup>3<sup>*j*</sup>5<sup>*k*</sup>, for some non-negative integers *i*, *j*, and *k*.

Write a function that computes the *n*th smallest Hamming number. 

Specifically:

  - The first smallest Hamming number is 1 = 2<sup>0</sup>3<sup>0</sup>5<sup>0</sup>
  - The second smallest Hamming number is 2 = 2<sup>1</sup>3<sup>0</sup>5<sup>0</sup>
  - The third smallest Hamming number is 3 = 2<sup>0</sup>3<sup>1</sup>5<sup>0</sup>
  - The fourth smallest Hamming number is 4 = 2<sup>2</sup>3<sup>0</sup>5<sup>0</sup>
  - The fifth smallest Hamming number is 5 = 2<sup>0</sup>3<sup>0</sup>5<sup>1</sup>

The 20 smallest Hamming numbers are given in example test fixture.

Your code should be able to compute all of the smallest 5,000 (Clojure: 2000, NASM: 13282) Hamming numbers without timing out.

[1]:https://en.wikipedia.org/wiki/Regular_number"""

from heapq import heappush, heappop
from itertools import islice


def h():
    heap = [1]
    while True:
        h = heappop(heap)
        while heap and h == heap[0]:
            heappop(heap)
        for m in [2, 3, 5]:
            heappush(heap, m * h)
        yield h

def hamming(n):
    return list(islice(h(), n - 1, n))[0]
  
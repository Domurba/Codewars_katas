#2021-09-21 14:22:44.854000+00:00
"""Description:
------------
A [triangle number](https://en.wikipedia.org/wiki/Triangular_number) is a number where *n* objects form an equilateral triangle (it's a bit hard to explain).  For example, 6 is a triangle number because you can arrange 6 objects into an equilateral triangle:
```
  1
 2 3
4 5 6
```
8 is not a triangle number because 8 objects do not form an equilateral triangle:
```
   1
  2 3
 4 5 6
7 8
```
In other words, the *n*th triangle number is equal to the sum of the *n* natural numbers from 1 to *n*.

Your task:
----------
Check if a given input is a valid triangle number.  Return true if it is, false if it is not (note that any non-integers, including non-number types, are not triangle numbers).

You are encouraged to develop an effective algorithm: test cases include really big numbers.

Assumptions:
------------
You may assume that the given input, if it is a number, is always positive.

Notes:
------
0 and 1 are triangle numbers."""

from math import sqrt

def is_triangle_number(number):
    if type(number) is not bool and isinstance(number, int):
        return not bool(sqrt(8 * number + 1) % 1)
    return False
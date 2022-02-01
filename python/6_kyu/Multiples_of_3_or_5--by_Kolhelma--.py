#2022-01-25 09:46:57.447000+00:00
"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 **below** the number passed in. 
Additionally, if the number is negative, return 0 (for languages that do have them).

**Note:** If the number is a multiple of **both** 3 and 5, only count it *once*.
  
***Courtesy of projecteuler.net** ([Problem 1](https://projecteuler.net/problem=1))*
"""

def solution(n):
    num1, num2 = 3, 5
    return sum(i for i in range(n) if (i % num1) == 0 or (i % num2) == 0)
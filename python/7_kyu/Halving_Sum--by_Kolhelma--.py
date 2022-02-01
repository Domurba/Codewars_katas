#2021-09-03 12:45:00.291000+00:00
"""## Task

Given a positive integer `n`, calculate the following sum: 

```
n + n/2 + n/4 + n/8 + ...
``` 

All elements of the sum are the results of integer division.

## Example

```
25  =>  25 + 12 + 6 + 3 + 1 = 47
```"""

def halving_sum(n): 
    print (n)
    s = n
    while n > 1.99:
        n = n // 2
        s += n
    return s
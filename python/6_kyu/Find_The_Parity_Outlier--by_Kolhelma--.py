#2021-09-18 09:28:55.125000+00:00
"""You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer `N`. Write a method that takes the array as an argument and returns this "outlier" `N`.

## Examples

```python
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
```"""

def find_outlier(integers):
    if sum([integers[i] | 1 > integers[i] for i in range(3)]) <= 1:
        for i in integers:
            if i | 1 > i:
                return i
    else:
        for i in integers:
            if i | 1 <= i:
                return i
        
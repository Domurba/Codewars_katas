#2021-08-14 15:38:53.536000+00:00
"""## Snail Sort

Given an `n x n` array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

```
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
```

For better understanding, please follow the numbers of the next array consecutively:

```
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
```

This image will illustrate things more clearly:

<img src="http://www.haan.lu/files/2513/8347/2456/snail.png" />

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array `[[]]`."""

import numpy


def add_edges_to_list(a):
    SL = []
    SL.append(a[0])
    for i in range(1, len(a)):
        SL.append([a[i][len(a)-1]])
    for i in reversed(range(0, len(a)-1)):
        SL.append([a[len(a)-1][i]])
    for i in reversed(range(1, len(a)-1)):
        SL.append([a[i][0]])
    return list(numpy.concatenate(SL).flat)


def remove_edges(a):
    del a[0]
    for i in range(0, len(a)):
        del a[i][len(a)]
    del a[len(a)-1]
    for i in range(0, len(a)):
        del a[i][0]

def snail(MAP):
    EL = []
    if len(MAP) == 1:
        EL.append(MAP[0])
    elif len(MAP)%2 == 0:
        while len(MAP) > 1:
            EL.append(add_edges_to_list(MAP))
            remove_edges(MAP)
    else:
        while len(MAP) > 1:
            EL.append(add_edges_to_list(MAP))
            remove_edges(MAP)
        EL.append(MAP[0])
    return list(numpy.concatenate(EL).flat)
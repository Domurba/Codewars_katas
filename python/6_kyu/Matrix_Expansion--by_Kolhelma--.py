#2021-10-09 13:30:47.432000+00:00
"""Expansion is performed for a given 2x2 matrix.

```
[
  [1,2],
  [5,3]
]
```

After expansion:

```
[
  [1,2,a],
  [5,3,b],
  [c,d,e]
]
```

- a = 1 + 2 = 3
- b = 5 + 3 = 8
- c = 5 + 1 = 6
- d = 3 + 2 = 5
- e = 1 + 3 = 4

Final result:

```
[
  [1,2,3],
  [5,3,8],
  [6,5,4]
]
```

## TASK

Let expansion be a function which takes two arguments:
- A: given NxN matrix
- n: number of expansions
"""

import numpy as np

def expansion(matrix, n):
    matrix = np.array(matrix) 
    for _ in range(n):
        side = np.sum(matrix, axis=1)
        bottom = np.append(np.sum(matrix, axis=0),  sum(matrix.diagonal()))
        matrix = np.append(matrix, np.reshape(side, (len(side),1)), axis=1)
        matrix = np.append(matrix, [bottom], axis=0)
    return matrix.tolist()
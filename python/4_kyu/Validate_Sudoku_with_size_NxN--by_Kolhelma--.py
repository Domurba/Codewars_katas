#2021-10-13 10:15:15.250000+00:00
"""Given a Sudoku data structure with size `NxN, N > 0 and √N == integer`, write a method to validate if it has been filled out correctly.


The data structure is a multi-dimensional Array, i.e:
```
[
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],
  
  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],
  
  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]
```

**Rules for validation**

- Data structure dimension: `NxN` where `N > 0` and `√N == integer`
- Rows may only contain integers: `1..N (N included)`
- Columns may only contain integers: `1..N (N included)`
- *'Little squares'* (`3x3` in example above) may also only contain integers: `1..N (N included)`
"""

from math import sqrt
from itertools import chain


class Sudoku(object):
    def __init__(self, data):
        self.data = data
    def is_valid(self):
        length = len(self.data)
        root = int(sqrt(length))
        if not all(len(row) == length for row in self.data) \
        or not all((type(i) == int and i in range(1, length + 1) for i in chain(*(self.data)))):
            return False
        else:
            for i in range(0,length):
                if len(set(self.data[i])) != length:
                    return False
                if len(set([nr[i] for nr in self.data])) != length:
                    return False
            for i in range(0, length, root):
                for j in range(0,length, root):
                    if len(set(chain(*(self.data[i+k][j:j+root] for k in range(root))))) != length:
                        return False
            return True
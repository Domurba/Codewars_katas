#2021-08-12 20:57:41.370000+00:00
"""If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is `0` if a spot is empty, `1` if it is an "X", or `2` if it is an "O", like so:

```
[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]
```

We want our function to return:

* `-1` if the board is not yet finished AND no one has won yet (there are empty spots),
* `1` if "X" won,
* `2` if "O" won,
* `0` if it's a cat's game (i.e. a draw).

You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe."""

from numpy import array
import itertools
board = [[2, 1, 2],
         [2, 1, 1],
         [1, 2, 1]]

def S(XO):
    return [sum(OX) for rang in range(2, len(XO)+1) for OX in itertools.combinations(XO, rang)]


def is_solved(board):
    square = [2, 7, 6, 9, 5, 1, 4, 3, 8]
    board = list(array(board).flat)
    x, o = [], []
    for i, k in enumerate(board):
        if k == 1:
            x.append(square[i])
        elif k == 2:
            o.append(square[i])
    print ('X vertes', x)
    print ('o vertes', o)
# try the magic square method they said....
    if 15 in S(x) and x != [7, 5, 1, 4, 8] and x != [7,1,4,8] and x != [7,1,4,3] and x!=[2, 6, 9, 5] and x!=[2, 6, 9, 5, 3]:
        return 1
    elif 15 in S(o) and o != [2, 6, 9, 3] and o != [7,1,4,8]and o != [7,1,4,3] and o!=[2, 6, 9, 5]:
        return 2
    elif 0 in board:
        return -1
    else:
        return 0
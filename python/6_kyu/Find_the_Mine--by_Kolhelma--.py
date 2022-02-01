#2021-09-21 15:21:55.238000+00:00
"""You've just discovered a square (NxN) field and you notice a warning sign. The sign states that there's a single bomb in the 2D grid-like field in front of you. 

Write a function `mineLocation`/`MineLocation` that accepts a 2D array, and returns the location of the mine. The mine is represented as the integer `1` in the 2D array. Areas in the 2D array that are not the mine will be represented as `0`s. 

The location returned should be an array (`Tuple<int, int>` in C#) where the first element is the row index, and the second element is the column index of the bomb location (both should be 0 based). All 2D arrays passed into your function will be square (NxN), and there will only be one mine in the array.

### Examples:
`mineLocation( [ [1, 0, 0], [0, 0, 0], [0, 0, 0] ] )` => returns `[0, 0]` <br/>
`mineLocation( [ [0, 0, 0], [0, 1, 0], [0, 0, 0] ] )` => returns `[1, 1]` <br/>
`mineLocation( [ [0, 0, 0], [0, 0, 0], [0, 1, 0] ] )` => returns `[2, 1]`"""

import pandas as pd


def mineLocation(field):
    df = pd.DataFrame(field)
    col = df.loc[df.isin([1]).any()].index[0].tolist()
    for i in range(len(field)):
        if df.index[df[i] == 1].tolist():
            row = df.index[df[i] == 1].tolist()
    return [int(row[-1]), col]
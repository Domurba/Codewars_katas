#2021-09-16 12:13:19.022000+00:00
"""Given the triangle of consecutive odd numbers:

```
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
```

Calculate the sum of the numbers in the n<sup>th</sup> row of this triangle (starting at index 1) e.g.: (**Input --> Output**)

```
1 -->  1
2 --> 3 + 5 = 8
```

"""

select n*n*n as res from nums
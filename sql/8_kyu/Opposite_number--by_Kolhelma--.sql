#2021-09-16 12:17:47.990000+00:00
"""Very simple, given an integer or a floating-point number, find its opposite.

Examples:
```
1: -1
14: -14
-34: 34
```

~~~if:sql
You will be given a table: `opposite`, with a column: `number`. Return a table with a column: `res`.
~~~"""

select -1* number as res from opposite
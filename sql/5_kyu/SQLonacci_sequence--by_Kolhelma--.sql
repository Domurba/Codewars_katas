#2021-10-26 09:09:26.862000+00:00
"""Yes it's Fibonacci yet again ! But this time it's SQL.

You need to create a select statement which will produce first 90 Fibonnacci numbers. The column name is - `number`

Fibbonaccii sequence is:
```
 0, 1, 1, 2, 3, 5, 8, 13, ..., 89, 144, 233, 377, ...
```
where 
```
f(0) = 0
f(1) = 1
...
f(n) = f(n-1) + f(n-2)
```

Have fun!"""

with recursive fb(number,b) as (
select 0::bigint, 1::bigint
  union
select b, number + b
  from fb where b < 1779979416004714201
) select number from fb
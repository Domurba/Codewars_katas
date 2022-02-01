#2021-09-22 10:55:09.721000+00:00
"""```if-not:sql
Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).
```

```if:sql
Given a database of first and last IPv4 addresses, calculate the number of addresses between them (including the first one, excluding the last one).

## Input

~~~
---------------------------------
|     Table    | Column | Type  |
|--------------+--------+-------|
| ip_addresses | id     | int   |
|              | first  | text  |
|              | last   | text  |
---------------------------------
~~~

## Output

~~~
-------------------------
|   Column    |  Type   |
|-------------+---------|
| id          | int     |
| ips_between | bigint  |
-------------------------
~~~
```

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

___

## Examples

```python
ips_between("10.0.0.0", "10.0.0.50")  ==   50 
ips_between("10.0.0.0", "10.0.1.0")   ==  256 
ips_between("20.0.0.10", "20.0.1.0")  ==  246
```
```javascript
ipsBetween("10.0.0.0", "10.0.0.50")  ===   50 
ipsBetween("10.0.0.0", "10.0.1.0")   ===  256 
ipsBetween("20.0.0.10", "20.0.1.0")  ===  246
```
```sql
   first    |    last     | ips_between
------------+-------------+-------------
 '10.0.0.0' | '10.0.0.50' |      50 
 '10.0.0.0' |  '10.0.1.0' |     256 
'20.0.0.10' |  '20.0.1.0' |     246
```
```typescript
ipsBetween("10.0.0.0", "10.0.0.50")  ===   50 
ipsBetween("10.0.0.0", "10.0.1.0")   ===  256 
ipsBetween("20.0.0.10", "20.0.1.0")  ===  246
```
```julia
ipsbetween("10.0.0.0", "10.0.0.50")  ==   50 
ipsbetween("10.0.0.0", "10.0.1.0")   ==  256 
ipsbetween("20.0.0.10", "20.0.1.0")  ==  246
```
```rust
ips_between("10.0.0.0", "10.0.0.50") ==  50 
ips_between("10.0.0.0", "10.0.1.0")  == 256 
ips_between("20.0.0.10", "20.0.1.0") == 246
```"""

def ips_between(start, end):
    print (end, start)
    start, end, ret = start.split("."), end.split("."), 0
    for n in range(3, 0, -1):
        ret += int(end[3 - n :: 4][0]) * 256 ** n - int(start[3 - n :: 4][0]) * 256 ** n
    return ret + int(end[3]) - int(start[3])
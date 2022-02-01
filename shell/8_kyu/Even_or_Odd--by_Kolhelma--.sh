#2021-09-13 10:31:17.833000+00:00
"""```if-not:sql,shell
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
```
```if:sql
## SQL Notes:
You will be given a table, `numbers`, with one column `number`.</br>

Return a table with a column `is_even` containing "Even" or "Odd" depending on `number` column values.

### numbers table schema
* number INT

### output table schema
* is_even STRING
```
```if:shell
Write a script that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
```"""

#!/usr/bin/sh


if [ $(( $1 % 2)) -eq 0 ]
then
  echo "Even"
else
  echo "Odd"
fi
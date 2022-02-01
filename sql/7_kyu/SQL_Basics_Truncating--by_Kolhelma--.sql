#2021-10-23 10:01:27.259000+00:00
"""Given the following table 'decimals':

### decimals table schema

* id
* number1
* number2

Return a table with a single column `towardzero` where the values are the result of number1 + number2 truncated towards zero."""

SELECT trunc(number1 + number2) as towardzero from decimals
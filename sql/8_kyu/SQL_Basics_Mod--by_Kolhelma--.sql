#2021-09-16 12:24:50.741000+00:00
"""Given the following table 'decimals':

** decimals table schema **
* id
* number1
* number2

Return a table with one column (mod) which is the output of number1 modulus number2."""

SELECT number1 % number2 as mod from decimals
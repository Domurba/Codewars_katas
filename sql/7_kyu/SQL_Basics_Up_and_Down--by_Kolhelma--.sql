#2021-11-30 10:14:14.089000+00:00
"""Given a table of random numbers as follows:

### numbers table schema

* id
* number1
* number2


Your job is to return table with similar structure and headings, where if the sum of a column is odd, the column shows the minimum value for that column, and when the sum is even, it shows the max value. You must use a case statement.

### output table schema

* number1
* number2"""

SELECT 
CASE 
WHEN SUM(number1) % 2 = 0 THEN max(number1)
else MIN(number1)
END number1,
CASE 
WHEN SUM(number2) % 2 = 0 THEN MAX(number2)
ELSE MIN(number2)
END number2
FROM NUMBERS

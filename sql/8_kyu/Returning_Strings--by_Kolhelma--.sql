#2021-09-14 13:50:44.553000+00:00
"""~~~if:sql
Write a select statement that takes `name` from `person` table and return `"Hello, <name> how are you doing today?"` results in a column named `greeting`
~~~
~~~if-not:sql
Make a function that will return a greeting statement that uses an input; your program should return, `"Hello, <name> how are you doing today?"`.
~~~

*[Make sure you type the exact thing I wrote or the program may not execute properly]*

"""

SELECT CONCAT('Hello, ' ,name, ' how are you doing today?') as greeting from person 
#2021-08-21 13:13:18.773000+00:00
"""This kata is inspired by [SQL Basics: Simple PIVOTING data](https://www.codewars.com/kata/sql-basics-simple-pivoting-data/sql) by [matt c](https://www.codewars.com/users/matt%20c). 

You need to build a pivot table WITHOUT using CROSSTAB function. Having two tables `products` and `details` you need to select a pivot table of products with counts of details occurrences (possible details values are `['good', 'ok', 'bad']`.

Results should be ordered by product's `name`.

Model schema for the kata is:

![schema](http://i.imgur.com/81Ww3YH.png)

your query should return table with next columns 

* name
* good
* ok
* bad

Compare your table to the expected table to view the expected results."""

SELECT p.name, 
  sum(CASE d.detail when 'good' then +1 else 0 end) as good,
  sum(CASE d.detail when 'ok' then +1 else 0 end) as ok,
  sum(CASE d.detail when 'bad' then +1 else 0 end) as bad
from products p join details d on d.product_id = p.id
group by p.name
order by p.name
  
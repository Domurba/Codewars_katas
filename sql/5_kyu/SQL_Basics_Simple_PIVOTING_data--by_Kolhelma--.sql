#2021-10-12 13:19:11.950000+00:00
"""For this challenge you need to PIVOT data. You have two tables, products and details. Your task is to pivot the rows in products to produce a table of products which have rows of their detail. Group and Order by the name of the Product.


### Tables and relationship below:
<img src="http://i.imgur.com/81Ww3YH.png" />


You must use the CROSSTAB statement to create a table that has the schema as below:

##### CROSSTAB table.
- name
- good
- ok
- bad

Compare your table to the expected table to view the expected results. 

[more info can be found here](https://www.postgresql.org/docs/9.2/static/tablefunc.html)"""

CREATE EXTENSION tablefunc;

CREATE VIEW ct as 
SELECT p.name, d.detail, count(1) as cnt
from details d
join products p on d.product_id = p.id
GROUP BY p.name, d.detail;

SELECT * FROM crosstab( 
$$ SELECT name, detail, cnt
  from ct
  ORDER BY 1,2$$
) AS ct ("name" text, "bad" bigint, "good" bigint, "ok" bigint )
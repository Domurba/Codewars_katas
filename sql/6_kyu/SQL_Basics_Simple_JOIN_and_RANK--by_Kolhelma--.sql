#2021-10-07 09:15:30.083000+00:00
"""For this challenge you need to create a simple SELECT statement that will return all columns from the `people` table, and join to the `sales` table so that you can return the COUNT of all sales and RANK each person by their sale_count.

### people table schema
- id
- name

### sales table schema
- id
- people_id
- sale
- price

You should return all people fields as well as the sale count as "sale_count" and the rank as "sale_rank".

> NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing."""

select p.id, p.name, 
count(s.id) as sale_count, rank() over(order by count(s.id)) sale_rank 
from people p
join sales s on s.people_id = p.id
group by p.id, p.name
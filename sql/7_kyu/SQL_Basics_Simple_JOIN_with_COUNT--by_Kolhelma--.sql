#2021-08-16 11:03:42.479000+00:00
"""For this challenge you need to create a simple SELECT statement that will return all columns from the `people` table, and join to the `toys` table so that you can return the COUNT of the toys

### people table schema
- id
- name

### toys table schema
- id
- name
- people_id

You should return all people fields as well as the toy count as "toy_count".

> NOTE: You're solution should use pure SQL. Ruby is used within the test cases to do the actual testing."""

select p.id, p.name, count(t.name) as toy_count from people p
join toys t on p.id = t.people_id
group by p.id;
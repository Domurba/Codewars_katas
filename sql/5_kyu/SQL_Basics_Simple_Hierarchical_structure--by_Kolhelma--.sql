#2021-10-25 16:19:26.716000+00:00
"""For this challenge you need to create a RECURSIVE Hierarchical query. You have a table `employees` of employees, you must order each employee by level. You must use a WITH statement and name it `employee_levels` after that has been defined you must select from it.

A Level is in correlation what manager managers the employee. e.g. an employee with a manager_id of NULL is at level 1 and then direct employees with the employee at level 1 will be level 2.

### employees table schema
- id
- first_name
- last_name
- manager_id (can be NULL)

### resultant schema
- level
- id
- first_name
- last_name
- manager_id (can be NULL)


>NOTE: refer to the `Results: expected` table if you're stuck with how it should be displayed."""

with recursive employee_levels as (
  select 
    1 as level,
    e1.id, 
    e1.first_name, 
    e1.last_name, 
    e1.manager_id
  from employees e1
  where e1.id = 1
UNION ALL
  SELECT
  level + 1,
  e2.id, 
  e2.first_name, 
  e2.last_name, 
  e2.manager_id
  from employees e2
  join employee_levels el on el.id = e2.manager_id
)
select * from employee_levels
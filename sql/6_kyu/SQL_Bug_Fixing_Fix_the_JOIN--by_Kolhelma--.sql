#2021-08-20 09:36:38.635000+00:00
"""Oh no! Timmys been moved into the database divison of his software company but as we know Timmy loves making mistakes. Help Timmy keep his job by fixing his query...

Timmy works for a statistical analysis company and has been given a task of calculating the highest average salary for a given job, the sample is compiled of 100 applicants each with a job and a salary. Timmy must display each unique job, the total average salary, the total people and the total salary and order by highest average salary. Timmy has some bugs in his query, help Timmy fix his query so he can keep his job!

### people table schema
- id
- name

### job table schema
- id
- people_id
- job_title
- salary

### resultant table schema
- job_title (unique)
- average_salary (float, 2 dp)
- total_people (int)
- total_salary (float, 2 dp)


> NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing."""

SELECT 
  j.job_title,
  round(avg(salary),2)::float as average_salary,
  COUNT(p.id) as total_people,
  round(sum(salary),2)::float as total_salary
FROM people p
JOIN job j on p.id = j.people_id
  GROUP BY j.job_title
  ORDER BY average_salary DESC
  
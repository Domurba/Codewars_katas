#2021-10-13 20:38:56.988000+00:00
"""For this challenge you need to create a simple GROUP BY statement, you want to group all the people by their age and count the people who have the same age.

### people table schema
- id
- name
- age

### select table schema
- age [group by]
- people_count (people count)


> NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing."""

SELECT age, count(age) as people_count
FROM people
GROUP BY age
#2021-11-30 10:52:24.049000+00:00
"""For this challenge you need to create a simple MIN / MAX statement that will return the Minimum and Maximum ages out of all the people.


### people table schema
- id
- name
- age

### select table schema
- age_min (minimum of ages)
- age_max (maximum of ages)


> NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing."""

SELECT min(age) AS age_min, max(age) as age_max from people
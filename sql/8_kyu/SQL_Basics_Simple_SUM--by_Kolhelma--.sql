#2021-09-16 09:26:57.772000+00:00
"""For this challenge you need to create a simple SUM statement that will sum all the ages.


### people table schema
- id
- name
- age

### select table schema
- age_sum (sum of ages)


> NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing.

> NOTE2: You need to use ALIAS for creating age_sum"""

SELECT sum(age) as age_sum from people

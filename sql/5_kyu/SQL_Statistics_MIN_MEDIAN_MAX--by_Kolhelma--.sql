#2021-10-19 12:19:05.393000+00:00
"""For this challenge you need to create a simple SELECT statement. Your task is to calculate the MIN, MEDIAN and MAX scores of the students from the results table.


### Tables and relationship below:
<image src="http://i.imgur.com/Qdt9DqU.png" />

### Resultant table:
- min
- median
- max"""

SELECT min(score) as min, PERCENTILE_CONT(0.5) WITHIN GROUP(ORDER BY score) as median,
max(score) as max from result
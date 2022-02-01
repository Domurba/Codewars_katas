#2021-09-29 09:01:29.122000+00:00
"""For this challenge you need to create a simple query to display each unique clan with their total points and ranked by their total points.

### people table schema
- name
- points
- clan  

You should then return a table that resembles below
### select on
- rank
- clan
- total_points
- total_people

The query must rank each clan by their total_points, you must return each unqiue clan and if there is no clan name (i.e. it's an empty string) you must replace it with `[no clan specified]`, you must sum the total_points for each clan and the total_people within that clan.

##Note
The data is loaded from the live leaderboard, this means values will change but also could cause the kata to time out retreiving the information.

> NOTE: You're solution should use pure SQL. Ruby is used within the test cases to do the actual testing."""

SELECT rank()over(order by sum(points) desc)rank, 
coalesce(NULLIF(clan,''), '[no clan specified]') as clan, sum(points) as total_points, count(people) as total_people
from people
group by clan
order by total_points desc
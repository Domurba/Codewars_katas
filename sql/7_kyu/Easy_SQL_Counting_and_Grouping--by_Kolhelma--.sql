#2021-10-13 08:20:54.708000+00:00
"""Given a demographics table in the following format:

** demographics table schema **
* id
* name
* birthday
* race

you need to return a table that shows a count of each race represented, ordered by the count in descending order as:

** output table schema **
* race
* count"""

SELECT race, count(race) as count from demographics 
group by race
order by count desc
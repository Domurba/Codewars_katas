#2021-09-16 12:48:55.776000+00:00
"""Given a demographics table in the following format:

** demographics table schema **
* id
* name
* birthday
* race

you need to return the same table where all letters are lowercase in the race column."""

select id, name, birthday, lower(race) as race from demographics
#2021-10-18 07:57:20.328000+00:00
"""Given a demographics table in the following format:

** demographics table schema **
* id
* name
* birthday
* race

you need to return the same table where all text fields (name & race) are changed to the bit length of the string."""

SELECT id, BIT_LENGTH(NAME) as name, birthday, BIT_LENGTH(RACE) as race from demographics 
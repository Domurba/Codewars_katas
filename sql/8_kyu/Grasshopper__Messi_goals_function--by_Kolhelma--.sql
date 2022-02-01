#2021-09-16 12:16:31.412000+00:00
"""# Messi goals function

[Messi](https://en.wikipedia.org/wiki/Lionel_Messi) is a soccer player with goals in three leagues: 

- LaLiga
- Copa del Rey
- Champions

Complete the function to return his total number of goals in all three leagues.

Note: the input will always be valid.

For example:

```
5, 10, 2  -->  17
```
"""

SELECT la_liga_goals + copa_del_rey_goals +champions_league_goals as res from goals 
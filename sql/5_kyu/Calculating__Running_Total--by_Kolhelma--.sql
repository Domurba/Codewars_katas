#2021-10-25 09:53:45.650000+00:00
"""### Description

Given a `posts` table that contains a `created_at` timestamp column write a query that returns date (without time component), a number of posts for a given date and a running (cumulative) total number of posts up until a given date. The resulting set should be ordered chronologically by `date`.

### Desired Output

The resulting set should look similar to the following:

```
date       | count | total
-----------+-------+-------
2017-01-26 |    20 |    20
2017-01-27 |    17 |    37
2017-01-28 |     7 |    44
2017-01-29 |     8 |    52
...
```

* date - (DATE) date
* count - (INT) number of posts for a date
* total - (INT) a running (cumulative) number of posts up until a date
"""

select 
created_at::date as date,
count(posts),
sum(count(posts)::int) OVER (order by created_at::date) as total
from posts
group by created_at::date
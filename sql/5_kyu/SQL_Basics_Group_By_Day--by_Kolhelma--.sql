#2021-09-24 09:32:11.917000+00:00
"""There is an `events` table used to track different key activities taken on a website. For this task you need to:

* find the entries whose `name` equals `"trained"`
* group them by the `day` the activity happened (the date part of the `created_at` timestamp) and their `description`'s
* the 2 aforementioned fields should be returned together with the number of grouped entries in a column called `count`
* the result should also be sorted by `day`

### "events" table schema

* `id` (bigint)
* `name` (text)
* `created_at` (timestamp)
* `description` (text)

### expected result schema

* `day` (date)
* `description` (text)
* `count` (numeric)"""

SELECT TO_CHAR(created_at, 'YYYY-MM-DD')::date as day,
description,
count(description)

from events
WHERE events.name = 'trained'
GROUP BY day, description, events.name
order by day, description
#2021-10-11 12:11:30.629000+00:00
"""Your task is to create a SQL query which returns the maximum number of simultaneous uses of a service. Each usage ("visit") is logged with its entry and exit timestamps in a "visits" table structured as follows:
```
id          primary key
entry_time  timestamp of visit start
exit_time   timestamp of visit end
```
A visit starts at _entry time_ and ends at _exit time_. At exactly _exit time_ the visit is considered to have already finished. The _visits_ table always contains at least one entry. Your query should return a single row, containing the following columns:
```
when_happened  earliest timestamp when there were visits_count concurrent visits
visits_count   maximum count of overlapping visits
```"""

select vs.entry_time as when_happened,
(select count(1) from visits v where vs.entry_time between v.entry_time and v.exit_time- interval '1 second')
as visits_count
from visits vs
order by visits_count desc
limit 1
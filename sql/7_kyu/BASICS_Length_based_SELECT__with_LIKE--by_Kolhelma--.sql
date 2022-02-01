#2021-10-15 13:56:54.068000+00:00
"""You will need to create SELECT statement in conjunction with LIKE.

Please list people which have first_name with at least 6 character long


### names table schema
- id
- first_name
- last_name

### results table schema
- first_name
- last_name"""

Select first_name, last_name
FROM names
where first_name like '%______%'
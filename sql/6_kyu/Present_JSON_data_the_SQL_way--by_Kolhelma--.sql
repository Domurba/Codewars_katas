#2021-09-30 10:08:11.132000+00:00
"""## Task

Given the database where users are stored in JSON format, fetch the records splitting the data into separate columns.

## Notes
* The `private` field determines whether the user's email address should be publicly visible
* If the profile is private, `email_address` should equal `"Hidden"`
* The users may have multiple email addresses
* If no email addresses are provided, `email_address` should equal `"None"`
* If there're multiple email addresses, the first one should be shown
* The `date_of_birth` is in the `yyyy-mm-dd` format
* The `age` fields represents the user's age in years
* Order the result by the `first_name`, and `last_name` columns

___

## Input table

```
-------------------------
| Table | Column | Type |
|-------+--------+------|
| users | id     | int  |
|       | data   | json |
-------------------------
```

## JSON object format

```
--------------------------------------
|     Field       |       Type       |
|-----------------+------------------|
| first_name      | string           |
| last_name       | string           |
| date_of_birth   | string           |
| email_addresses | array of strings |
| private         | boolean          |
--------------------------------------
```

## Output table

```
------------------------
|    Column     | Type |
|---------------+------|
| first_name    | text |
| last_name     | text |
| age           | int  |
| email_address | text |
------------------------
```"""

SELECT 
data::json->>'first_name' as first_name,
data::json->>'last_name' as last_name,

extract(YEAR from AGE(current_date, to_date(data::json->>'date_of_birth', 'YYYY-MM-DD')))::INT AS AGE,

CASE 
  WHEN (data::json->>'private' = 'true') THEN 'Hidden'
  WHEN (data::json->>'private' = 'false') THEN coalesce(data::json#>>'{email_addresses,0}', 'None')
end as email_address
from users
ORDER BY first_name, last_name


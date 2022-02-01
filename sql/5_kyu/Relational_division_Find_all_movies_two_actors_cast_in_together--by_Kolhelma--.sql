#2021-09-26 11:08:16.981000+00:00
"""Given `film_actor` and `film` tables from the [DVD Rental](http://www.postgresqltutorial.com/postgresql-sample-database/) sample database find all movies both Sidney Crowe (`actor_id = 105`) 
and Salma Nolte (`actor_id = 122`) cast in together and order the result set alphabetically.

#### film schema

```
 Column     | Type                        | Modifiers
------------+-----------------------------+----------
title       | character varying(255)      | not null
film_id     | smallint                    | not null
```

#### film\_actor schema

```
 Column     | Type                        | Modifiers
------------+-----------------------------+----------
actor_id    | smallint                    | not null
film_id     | smallint                    | not null
last_update | timestamp without time zone | not null 
```

#### actor schema

```
 Column     | Type                        | Modifiers
------------+-----------------------------+----------
actor_id    | integer                     | not null 
first_name  | character varying(45)       | not null
last_name   | character varying(45)       | not null
last_update | timestamp without time zone | not null 
```

The desired output:

```
title
-------------
Film Title 1
Film Title 2
...

```

* `title` - Film title
"""

select f.title from 
film_actor fa
join film f
on f.film_id = fa.film_id
join actor a
on a.actor_id = fa.actor_id
where a.actor_id = 105 or a.actor_id = 122

group by f.title
having count(f.title) > 1
order by f.title
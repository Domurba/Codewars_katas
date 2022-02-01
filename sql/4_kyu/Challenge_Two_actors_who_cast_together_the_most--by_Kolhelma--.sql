#2021-11-25 19:49:39.862000+00:00
"""Given the the schema presented below find two actors who cast together 
the most and list titles of only those movies they were casting together. 
Order the result set alphabetically by the movie title.



#### Table film_actor

```
 Column     | Type                        | Modifiers
------------+-----------------------------+----------
actor_id    | smallint                    | not null
film_id     | smallint                    | not null
...
```

#### Table actor

```
 Column     | Type                        | Modifiers
------------+-----------------------------+----------
actor_id    | integer                     | not null 
first_name  | character varying(45)       | not null
last_name   | character varying(45)       | not null
...
```

#### Table film

```
 Column     | Type                        | Modifiers
------------+-----------------------------+----------
film_id     | integer                     | not null
title       | character varying(255)      | not null
...
```

#### The desired output:

```
first_actor | second_actor | title
------------+--------------+--------------------
John Doe    | Jane Doe     | The Best Movie Ever
...
```

* `first_actor` - Full name (First name + Last name separated by a space)
* `second_actor` - Full name (First name + Last name separated by a space)
* `title` - Movie title

**Note:** `actor_id` of the first_actor should be lower then `actor_id` of the second_actor
"""

WITH couple AS
(SELECT fa1.actor_id as id1, fa2.actor_id as id2, count(fa2.actor_id) as nr
FROM film_actor fa1, film_actor fa2
WHERE fa1.film_id = fa2.film_id and fa1.actor_id <> fa2.actor_id
GROUP BY fa1.actor_id, fa2.actor_id
ORDER BY nr DESC
LIMIT 1)

SELECT concat_ws(' ', a1.first_name, a1.last_name) as "first_actor", 
concat_ws(' ', a2.first_name, a2.last_name) as "second_actor", film.title

FROM actor a1, actor a2, film, couple cp
where cp.id1 = a1.actor_id and cp.id2 = a2.actor_id and film.film_id in
(select fa1.film_id from film_actor fa1, film_actor fa2
where fa1.film_id = fa2.film_id and fa1.actor_id = a1.actor_id and fa2.actor_id = a2.actor_id)


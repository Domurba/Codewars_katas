#2021-09-30 13:36:17.358000+00:00
"""The objective of this Kata is to show that you are proficient at string manipulation (and perhaps that you can use extensively subqueries).

You will use people table but will focus solely on the `name` column

---

|**name**	                    |
|:---------------------------:|
|Greyson Tate Lebsack Jr.     |
|Elmore Clementina O'Conner   |

---

you will be provided with a full name and you have to return the name in columns as follows.

---

|**name**	        |**first_lastname** |**second_lastname**|
| ------------|:---------:| ---------:|
|Greyson Tate	|Lebsack	  |Jr.        |
|Elmore	      |Clementina	|O'Conner   |

---

Note: Don't forget to remove spaces around names in your result.
Note: Due to multicultural context, if full name has more than 3 words, consider first 2 as name
"""

SELECT CASE
  WHEN cardinality(string_to_array(name, ' ')) = 4 THEN SPLIT_PART(name, ' ', 1) || ' ' || SPLIT_PART(name, ' ', 2)
  ELSE SPLIT_PART(name, ' ', 1)
END AS name,
split_part(name, ' ', array_upper(fn, 1)-1) as first_lastname,
split_part(name, ' ', array_upper(fn, 1)) as second_lastname
FROM (SELECT string_to_array(name, ' ') as fn, name FROM people) as ppl
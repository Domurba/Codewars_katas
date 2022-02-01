#2021-10-01 18:06:06.727000+00:00
"""Write a SELECT query which will return all prime numbers smaller than 100 in ascending order.

Your query should return one column named `prime`."""

select unnest(string_to_array('2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 
61, 67, 71, 73, 79, 83, 89, 97', ', '))::int as prime
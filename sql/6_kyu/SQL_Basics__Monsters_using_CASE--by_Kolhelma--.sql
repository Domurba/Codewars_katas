#2021-08-20 14:07:32.257000+00:00
"""You have access to two tables named top\_half and bottom\_half, as follows:

**top\_half schema**
* id
* heads
* arms

**bottom\_half schema**
* id
* legs
* tails

You must return a table with the format as follows:

**output schema**
* id
* heads
* legs
* arms
* tails
* species

The IDs on the tables match  to make a full monster. For heads, arms, legs and tails you need to draw in the data from each table.

For the species, if the monster has more heads than arms, more tails than legs, or both, it is a 'BEAST' else it is a 'WEIRDO'. This needs to be captured in the species column.

All rows should be returned (10).

Tests require the use of CASE. Order by species.

Please use pure SQL, only testing is done in Ruby."""

SELECT uh.id, uh.heads, bh.legs, uh.arms, bh.tails,
  CASE 
    WHEN heads > arms or tails > legs THEN 'BEAST'
    ELSE 'WEIRDO'
  END as Species
FROM top_half uh
JOIN bottom_half bh on bh.id = uh.id
order by Species
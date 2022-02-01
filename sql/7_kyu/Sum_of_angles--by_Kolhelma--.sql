#2021-10-14 19:36:59.229000+00:00
"""Find the total sum of internal angles (in degrees) in an n-sided simple polygon. N will be greater than 2."""

select (n-2)*180 as res from angle
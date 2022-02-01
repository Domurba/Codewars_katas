#2021-10-23 10:05:53.852000+00:00
"""Practise some SQL fundamentals by making a simple database on a topic you feel familiar with. Or use mine, populated with a wealth of Sailor Moon trivia.

### `sailorsenshi` schema
* id
* senshi_name
* real_name_jpn
* school_id
* cat_id

### `cats` schema
* id
* name

### `schools` schema
* id
* school


Return a results table - *sailor_senshi, real_name, cat* and *school* - of all characters, containing each character's high school, their civilian name and the cat who introduced them to their magical crime-fighting destiny.

Keep in mind some senshi were not initiated by a cat guardian and one is not in high school. The field can be left blank if this is the case."""

SELECT senshi_name as sailor_senshi, real_name_jpn as real_name, c.name as cat, s.school
FROM sailorsenshi ss
left JOIN cats c on ss.cat_id = c.id
left JOIN schools s on s.id = ss.school_id

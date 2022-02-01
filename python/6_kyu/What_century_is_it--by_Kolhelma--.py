#2021-10-19 09:01:38.256000+00:00
"""Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation. 

### Examples
```
"1999" --> "20th"
"2011" --> "21st"
"2154" --> "22nd"
"2259" --> "23rd"
"1124" --> "12th"
"2000" --> "20th"
```"""

from math import ceil
def what_century(year):
    nr = str(ceil(int(year)/100))
    dig = int(nr[-1])
    return nr + ('th' if nr in ['11','12','13'] else 'st' if dig == 1 else ('nd' if dig == 2 else ('rd' if dig == 3 else 'th')))
#2021-11-03 21:35:09.375000+00:00
"""Complete the  function `scramble(str1, str2)` that returns `true` if a portion of ```str1``` characters can be rearranged to match ```str2```, otherwise returns ```false```.

**Notes:**
* Only lower case letters will be used (a-z). No punctuation or digits will be included.
* Performance needs to be considered

```c
Input strings s1 and s2 are null terminated.
```

## Examples

```python
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
```
"""

from collections import Counter

def scramble(s1, s2):
    s1, s2 = Counter(s1), Counter(s2)
    for k,v in s2.items():
        if s1[k] < v:
            return False
    return True
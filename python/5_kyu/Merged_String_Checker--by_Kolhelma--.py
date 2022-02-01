#2022-01-09 08:33:11.723000+00:00
"""At a job interview, you are challenged to write an algorithm to check if a given string, `s`, can be formed from two other strings, `part1` and `part2`.

The restriction is that the characters in `part1` and `part2` should be in the same order as in `s`.

The interviewer gives you the following example and tells you to figure out the rest from the given test cases.

For example:

```
'codewars' is a merge from 'cdw' and 'oears':

    s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears
```"""

from collections import deque


def ln(wrd_i, p1c, p2c="DEFAULT"):
    if p2c != "DEFAULT":
        return len(p1c) >= wrd_i + 1 and len(p2c) >= wrd_i + 1
    return len(p1c) >= wrd_i + 1


def poppy(sc, p, same):
    for _ in range(same + 1):
        p.popleft(), sc.popleft()


def current_s(sc, p1c, p2c):
    same_l = 0
    for i, l in enumerate(sc):
        if ln(i, p1c, p2c) and p1c[i] == l and p2c[i] == l:
            same_l += 1
        elif ln(i, p1c) and p1c[i] == l:
            poppy(sc, p1c, same_l)
            same_l = 0
            break
        elif ln(i, p2c) and p2c[i] == l:
            poppy(sc, p2c, same_l)
            same_l = 0
            break
        else:
            sc.clear()
            break


def is_merge(sc, p1c, p2c):
    if len(sc) != len(p1c) + len(p2c):
        return False
    sc, p1c, p2c = deque(list(sc)), deque(list(p1c)), deque(list(p2c))
    while sc:
        current_s(sc, p1c, p2c)
    return not any([sc, p1c, p2c])
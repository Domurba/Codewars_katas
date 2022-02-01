#2021-11-05 15:49:03.625000+00:00
"""Your job is to write a function which increments a string, to create a new string.

- If the string already ends with a number, the number should be incremented by 1.
- If the string does not end with a number. the number 1 should be appended to the new string.

Examples:

`foo -> foo1`

`foobar23 -> foobar24`

`foo0042 -> foo0043`

`foo9 -> foo10`

`foo099 -> foo100`

*Attention: If the number has leading zeros the amount of digits should be considered.*
"""

from re import findall


def increment_string(strng):
    match = findall(r"(\d+$)", strng)
    if match:
        return strng.replace(match[0], "") + str(int(match[0]) + 1).zfill(len(match[0]))
    else:
        return strng + "1"
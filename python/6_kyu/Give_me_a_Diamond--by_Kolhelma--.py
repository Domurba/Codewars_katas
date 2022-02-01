#2021-09-21 11:33:24.969000+00:00
"""Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.

## Task

You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (`*`) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (`\n`).

Return `null/nil/None/...` if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.


## Examples

A size 3 diamond:

```
 *
***
 *
```

...which would appear as a string of `" *\n***\n *\n"`


A size 5 diamond:

```
  *
 ***
*****
 ***
  *
```

...that is: 
```
"  *\n ***\n*****\n ***\n  *\n"
```
"""

def diamond(n):
    if n % 2 == 0 or n < 0:
        return None
    ret = ""
    spaces = int(n / 2) * " "
    stars = int(n / n) * "*" + "\n"
    for i in range(int(n / 2) + 1):
        ret += spaces + stars
        spaces = spaces.replace(" ", "", 1)
        stars = stars.replace("\n", "")
        stars += "**\n"
    stars = stars.replace("\n", "", 1)
    for l in range(int(n / 2)):
        stars = stars.replace("*", " ", 1)
        ret += stars[: len(stars) - 3 - l] + "\n"
    return ret
        
    
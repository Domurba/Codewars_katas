#2021-11-12 19:19:03.243000+00:00
"""In this exercise, a string is passed to a method and a new string has to be returned with the first character of each word in the string.

For example:

```
"This Is A Test" ==> "TIAT"
```

Strings will only contain letters and spaces, with exactly 1 space between words, and no leading/trailing spaces."""

import re

def make_string(s):
    return "".join(re.findall(r"\b\w", s))
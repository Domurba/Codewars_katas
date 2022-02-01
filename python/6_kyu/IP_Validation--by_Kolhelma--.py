#2021-09-07 10:51:46.018000+00:00
"""Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between `0` and `255`, inclusive.


#### Valid inputs examples:
```
Examples of valid inputs:
1.2.3.4
123.45.67.89
```

#### Invalid input examples:
```
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
```

#### Notes:
- Leading zeros (e.g. `01.02.03.04`) are considered invalid
- Inputs are guaranteed to be a single string"""

import re
def is_valid_IP(strng):
    found = list(filter(None, re.findall(r"\b(?!0)(\d{1,3})\b", strng)))
    g = strng.split(".")
    for i in g:
        if i == "0":
            found.append(i)
        if not i.isdigit():
            return False
    if len(found) != 4:
        return False
    for i in found:
        if 255 < int(i) or int(i) < -1:
            return False
    return True
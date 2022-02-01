#2021-07-30 12:38:23.161000+00:00
"""Write a function that accepts a string, and returns true if it is in the form of a phone number. <br/>Assume that any integer from 0-9 in any of the spots will produce a valid phone number.<br/>

Only worry about the following format:<br/>
(123) 456-7890   (don't forget the space after the close parentheses) <br/> <br/>
Examples:

```
"(123) 456-7890"  => true
"(1111)555 2345"  => false
"(098) 123 4567"  => false
```
"""

import re
def valid_phone_number(phone_number):
    if re.match(r'\(\d\d\d\) \d\d\d-\d\d\d\d$' , phone_number):
        return True
    else:
        return False

#2021-09-21 11:53:38.553000+00:00
"""You need to write a password generator that meets the following criteria:

* 6 - 20 characters long
* contains at least one lowercase letter
* contains at least one uppercase letter
* contains at least one number
* contains only alphanumeric characters (no special characters)

Return the random password as a string.

**Note**: "randomness" is checked by counting the characters used in the generated passwords - all characters should have less than 50% occurance. Based on extensive tests, the normal rate is around 35%.

"""

import random
from string import digits, ascii_uppercase, ascii_lowercase

def password_gen():
    l = random.randint(3, 17)
    password = random.sample(digits + ascii_uppercase + ascii_lowercase, l)
    password += (random.sample(digits, 1)) + (random.sample(ascii_uppercase, 1)) + (random.sample(ascii_lowercase, 1))
    random.shuffle(password)
    return ''.join(password)
    
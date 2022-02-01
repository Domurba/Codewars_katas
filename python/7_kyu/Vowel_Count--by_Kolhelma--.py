#2021-07-08 09:03:25.242000+00:00
"""Return the number (count) of vowels in the given string. 

We will consider `a`, `e`, `i`, `o`, `u` as vowels for this Kata (but not `y`).

The input string will only consist of lower case letters and/or spaces.
"""

def get_count(input_str):
    num_vowels = 0
    balses="aeiou"
    for raides in input_str.lower():
        if raides in balses:
            num_vowels=num_vowels +1
    return num_vowels
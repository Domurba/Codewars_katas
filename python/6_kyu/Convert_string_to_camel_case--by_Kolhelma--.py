#2021-11-23 09:30:54.451000+00:00
"""Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized **only** if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). 

### Examples

`"the-stealth-warrior"` gets converted to `"theStealthWarrior"`  
`"The_Stealth_Warrior"` gets converted to `"TheStealthWarrior"`
"""

from re import split
def to_camel_case(text):
    txt = split(r'_|-', text)
    return txt[0] + "".join((i.title() for i in txt[1:]))
#2021-09-14 11:14:43.331000+00:00
"""Substitute two equal letters by the next letter of the alphabet (two letters convert to one):

    "aa" => "b", "bb" => "c", .. "zz" => "a".

The equal letters do _not_ have to be adjacent.  
Repeat this operation until there are no possible substitutions left.  
Return a string.

Example:

    let str = "zzzab"
        str = "azab"
        str = "bzb"
        str = "cz"
    return "cz"

#### Notes

* The order of letters in the result is not important.
* The letters `"zz"` transform into `"a"`.
* There will only be lowercase letters.

If you like this kata, check out another one: [Last Survivor Ep.3](https://www.codewars.com/kata/60a2d7f50eee95000d34f414)"""

import re
def last_survivors(st):
    st = "".join(sorted(st))
    while bool(re.search(r"([a-z])\1", st)):
        st = re.sub(r"([a-z])\1", lambda x: str(chr(ord((x.group(0)[0])) + 1)), st)
        st = re.sub("{", "a", st)
        st = "".join(sorted(st))
    return st
#2021-09-20 18:21:27.090000+00:00
"""A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant). 

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation. 

```if:prolog
**Note for prolog users**: your task is to write a predicate **is_pangram/1** instead.
```"""


alph = "abcdefghijklmnopqrstuvwxyz"
def is_pangram(s):
    for l in alph:
        if l not in s.lower():
            return False
    return True
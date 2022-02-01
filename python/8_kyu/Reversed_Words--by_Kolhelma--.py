#2021-09-03 12:29:48.443000+00:00
"""Complete the solution so that it reverses all of the words within the string passed in. 

Example:

```
"The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"
```

"""

def reverse_words(s):
    l = s.split(" ")
    l.reverse()
    return " ".join(l)
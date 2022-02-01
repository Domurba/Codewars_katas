#2021-09-23 19:37:26.526000+00:00
"""Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return `true` if the string is valid, and `false` if it's invalid.

## Examples

```
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
```

## Constraints

`0 <= input.length <= 100`

~~~if-not:javascript,go
Along with opening (`(`) and closing (`)`) parenthesis, input may contain any valid ASCII characters.  Furthermore, the input string may be empty and/or not contain any parentheses at all.  Do **not** treat other forms of brackets as parentheses (e.g. `[]`, `{}`, `<>`).
~~~"""

def valid_parentheses(s):
    k = [i for i in s if i in "()"]
    try:
        len(exec("".join(k)))
    except SyntaxError:
        return False
    except TypeError:
        return True
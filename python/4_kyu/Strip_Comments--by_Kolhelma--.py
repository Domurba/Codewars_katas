#2021-11-18 18:16:42.630000+00:00
"""Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out. 

**Example:**

Given an input string of:
```
apples, pears # and bananas
grapes
bananas !apples
```

The output expected would be:
```
apples, pears
grapes
bananas
```

The code would be called like so:

```javascript
var result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
// result should == "apples, pears\ngrapes\nbananas"

```

```kotlin
var result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", charArrayOf('#', '!'))
// result should == "apples, pears\ngrapes\nbananas"

```

```coffeescript
result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\nograpes\nbananas"

```

```ruby
result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"

```

```crystal
result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"

```

```python
result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"

```

```csharp
string stripped = StripCommentsSolution.StripComments("apples, pears # and bananas\ngrapes\nbananas !apples", new [] { "#", "!" })
// result should == "apples, pears\ngrapes\nbananas"
```

```julia
result = stripcomments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
```"""

def solution(string, markers):
    string = string.split("\n")
    strings = []
    for part in string:
        if any(n in markers for n in part):
            for n in markers:
                part = part.split(n)[0]
            strings.append(part.strip())
        else:
            strings.append(part)
    return "\n".join(strings)
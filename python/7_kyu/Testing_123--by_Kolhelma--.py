#2021-12-30 12:13:17.917000+00:00
"""Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is `n: string`. Notice the colon and space in between.

**Examples:**

```csharp
number(List<string>()) // => List<string>()
number(List<string>{"a", "b", "c"}) // => ["1: a", "2: b", "3: c"]
```

```ruby
number [] # => []
number ["a", "b", "c"] # => ["1: a", "2: b", "3: c"]
```

```javascript
number([]) // => []
number(["a", "b", "c"]) // => ["1: a", "2: b", "3: c"]
```

```coffeescript
number [] # => []
number ['a', 'b', 'c'] # => ['1: a', '2: b', '3: c']
```

```python
number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]
```

```java
number(Arrays.asList()) # => []
number(Arrays.asList("a", "b", "c")) // => ["1: a", "2: b", "3: c"]
```

```haskell
number [] -- returns []
number ["a", "b", "c"] -- returns ["1: a", "2: b", "3: c"]
```

```r
number(c()) # => c()
number(c("a", "b", "c")) # => c("1: a", "2: b", "3: c")
```

```julia
number([]) # --> []
number(["a", "b", "c"]) # --> ["1: a", "2: b", "3: c"]
```
"""

def number(lines):
    return [f'{a}: {b}'for a,b in zip(range(1, len(lines) + 1), lines)]
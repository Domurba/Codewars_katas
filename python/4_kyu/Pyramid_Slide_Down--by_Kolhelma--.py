#2021-11-22 11:28:13.016000+00:00
"""### Lyrics...

Pyramids are amazing! Both in architectural and mathematical sense. If you have a computer, you can mess with pyramids even if you are not in Egypt at the time. For example, let's consider the following problem. Imagine that you have a pyramid built of numbers, like this one here:

```
   /3/
  \7\ 4 
 2 \4\ 6 
8 5 \9\ 3
```

### Here comes the task...

Let's say that the *'slide down'* is the maximum sum of consecutive numbers from the top to the bottom of the pyramid. As you can see, the longest *'slide down'* is `3 + 7 + 4 + 9 = 23`

Your task is to write a function `longestSlideDown` (in ruby/crystal/julia: `longest_slide_down`) that takes a pyramid representation as argument and returns its' __largest__ *'slide down'*. For example,

```haskell
longestSlideDown [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]  -> 23
```
```python
longestSlideDown([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) => 23
```
```javascript
longestSlideDown([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) => 23
```
```ruby
longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) => 23
```
```crystal
longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) => 23
```
```java
longestSlideDown [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]] => 23
```
```clojure
(longestSlideDown [[3] [7 4] [2 4 6] [8 5 9 3]]) => 23
```
```csharp
LongestSlideDown(new[] { new[] {3}, new[] {7, 4}, new[] {2, 4, 6}, new[] {8, 5, 9, 3} }); => 23
```
```rust
longest_slide_down(&[vec![3], vec![7, 4], vec![2, 4, 6], vec![8, 5, 9, 3]]) => 23
```
```julia
longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) => 23
```

### By the way...

My tests include some extraordinarily high pyramids so as you can guess, brute-force method is a bad idea unless you have a few centuries to waste. You must come up with something more clever than that.

(c) This task is a lyrical version of the __Problem 18__ and/or __Problem 67__ on [ProjectEuler](https://projecteuler.net).
"""

def longest_slide_down(pyramid):
    if len(pyramid) == 1: return pyramid[0][0]
    pyramid[-2] = [x + y for x, y in zip(pyramid[-2],[max(pyramid[-1][i], pyramid[-1][i - 1]) for i in range(1, len(pyramid[-1]))])]
    return longest_slide_down(pyramid[:-1])
#2022-01-06 07:37:48.432000+00:00
"""I love Fibonacci numbers in general, but I must admit I love some more than others. 

I would like for you to write me a function that when given a number (n)  returns the n-th number in the Fibonacci Sequence.

For example:

```javascript
   nthFibo(4) == 2
```
```coffeescript
   nthFibo(4) == 2
```
```ruby
   nth_fibonacci(4) == 2
```
```haskell
   fib 4 == 2
```
```python
   nth_fib(4) == 2
```
```csharp
   NthFib(4) == 2
```
```c
   nth_fib(4) == 2
```

Because 2 is the 4th number in the Fibonacci Sequence.

For reference, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two."""

def nth_fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return nth_fib(n-1) + nth_fib(n-2)
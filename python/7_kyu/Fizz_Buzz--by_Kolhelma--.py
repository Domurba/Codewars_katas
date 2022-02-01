#2021-10-25 16:51:32.934000+00:00
"""~~~if-not:scala
Return an array containing the numbers from 1 to N, where N is the parametered value.
~~~

~~~if:scala
Return a list containing the numbers from 1 to N, where N is the parametered value.
~~~

Replace certain values however if any of the following conditions are met:
* If the value is a multiple of 3: use the value "Fizz" instead
* If the value is a multiple of 5: use the value "Buzz" instead
* If the value is a multiple of 3 & 5: use the value "FizzBuzz" instead

N will never be less than 1.

Method calling example:
```python
fizzbuzz(3) -->  [1, 2, "Fizz"]
```
```haskell
fizzbuzz(3) -->  ["1", "2", "Fizz"]
```
```kotlin
fizzBuzz(3) -->  ["1", "2", "Fizz"]
```
```csharp
string[] result = FizzBuzz.GetFizzBuzzArray(3); // => [ "1", "2", "Fizz" ]
```
```prolog
fizzify(3, [1, 2, "Fizz"]).
```
```scala
FizzBuzz.fizzify(3) // List("1", "2", "Fizz")
```
"""

def fizzbuzz(n):
    return ['FizzBuzz' if l%3 == 0 and l%5 ==0 else 'Fizz' if l%3 == 0 else 'Buzz' if l%5==0 else l for l in range(1, n+1) ]
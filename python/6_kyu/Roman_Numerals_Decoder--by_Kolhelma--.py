#2021-11-12 15:22:09.395000+00:00
"""Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Example:

```javascript
solution('XXI'); // should return 21
```
```cpp
solution("XXI"); // => 21
```
```php
solution('XXI'); // should return 21
```
```coffeescript
solution('XXI') # should return 21
```

```ruby
solution('XXI') # should return 21
```

```python
solution('XXI') # should return 21
```

```haskell
solution "XXI" -- should return 21
```
```csharp
RomanDecode.Solution("XXI") -- should return 21
```
```typescript
solution('XXI'); // should return 21
```
```swift
solution("XXI") // should return 21
```
```Elixir
Solution.decode("XXI") # should return 21
```
```r
solution("XXI") # should return 21
```
```lua
romanDecoder("XXI") -- should return 21
```
```scala
Roman.decode("XXI") // should return 21
```
```clojure
(translate-roman-numerals "XXI") ;; should return 21
```
```kotlin
decode("XXI") // should return 21
```

Help:
```
Symbol	Value
I	      1
V	      5
X	      10
L	      50
C	      100
D	      500
M	      1,000
```

*Courtesy of rosettacode.org*
"""

letters = [('M',1000), ('CM',900), ('D',500), ('CD',400), ('C',100), ('XC',90),
           ('L',50), ('XL',40), ('X',10), ('IX',9), ('V',5), ('IV',4), ('I',1)]
def solution(rom):
    cumu = 0
    for l, v in letters:
        while rom[:len(l)] == l:
            rom = rom[len(l):]
            cumu += v
        if not rom: break
    return cumu
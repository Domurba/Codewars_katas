#2021-09-28 11:10:44.678000+00:00
"""In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Examples:

```javascript
permutations('a'); // ['a']
permutations('ab'); // ['ab', 'ba']
permutations('aabb'); // ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
```
```cpp
permutations("a"); // => vector<string> {"a"}
permutations("ab"); // => vector<string> {"ab", "ba"}
permutations("aabb"); // => vector<string> {"aabb", "abab", "abba", "baab", "baba", "bbaa"}
```
```php
permutations('a'); // => ['a']
permutations('ab'); // => ['ab', 'ba']
permutations('aabb'); // => ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
```
```ruby
permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
```
```python
permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
```
```haskell
permutations    "a" `shouldBe` ["a"]
permutations   "ab" `shouldBe` ["ab", "ba"]
permutations "aabb" `shouldBe` ["aabb","abab","abba","baab","baba","bbaa"]
```
```java
Permutations.singlePermutations("a") `shouldBe` ["a"]
Permutations.singlePermutations("ab") `shouldBe` ["ab", "ba"]
Permutations.singlePermutations("aabb") `shouldBe` ["aabb","abab","abba","baab","baba","bbaa"]
```
```csharp
Permutations.SinglePermutations("a"); // => new List {"a"}
Permutations.SinglePermutations("ab"); // => new List {"ab", "ba"}
Permutations.SinglePermutations("aabb"); // => new List {"aabb", "abab", "abba", "baab", "baba", "bbaa"}
```
```elixir
Kata.permutations("a") == ["a"]
Kata.permutations("ab") == ["ab","ba"]
Kata.permutations("aabb") == ["aabb","abab","abba","baab","baba","bbaa"]
```

The order of the permutations doesn't matter.
"""

from itertools import permutations as p
def permutations(string):
    print (string)
    return list(set(''.join(i) for i in list(p(string, len(string)))))
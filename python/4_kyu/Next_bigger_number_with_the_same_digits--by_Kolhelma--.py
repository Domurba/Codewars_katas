#2021-10-09 19:58:17.946000+00:00
"""Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

```
12 ==> 21
513 ==> 531
2017 ==> 2071
```
```swift
nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071
```

If the digits can't be rearranged to form a bigger number, return `-1` (or `nil` in Swift):

```
9 ==> -1
111 ==> -1
531 ==> -1
```
```swift
nextBigger(num: 9)   // returns nil
nextBigger(num: 111) // returns nil
nextBigger(num: 531) // returns nil
```"""

def next_bigger(n):
    try:    
        array = list(str(n))
        i = max(i for i in range(1, len(array)) if array[i - 1] < array[i])
        j = max(j for j in range(i, len(array)) if array[j] > array[i - 1])
        array[j], array[i - 1] = array[i - 1], array[j]
        array[i:] = reversed(array[i:])
        return int(''.join(array))
    except Exception:
        return -1
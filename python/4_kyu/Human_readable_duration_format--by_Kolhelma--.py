#2021-10-01 15:34:13.613000+00:00
"""Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns `"now"`. Otherwise,  the duration is expressed as a combination of `years`, `days`, `hours`, `minutes` and `seconds`.

It is much easier to understand with an example:

```Fortran
formatDuration (62)    // returns "1 minute and 2 seconds"
formatDuration (3662)  // returns "1 hour, 1 minute and 2 seconds"
```
```c
formatDuration (62)    // returns "1 minute and 2 seconds"
formatDuration (3662)  // returns "1 hour, 1 minute and 2 seconds"
```
```nasm
mov edi, 62
call fmtduration      ; RAX <- `1 minute and 2 seconds\0`

mov edi, 3662
call fmtduration      ; RAX <- `1 hour, 1 minute and 2 seconds\0`
```
```cpp
format_duration(62)    // returns "1 minute and 2 seconds"
format_duration(3662)  // returns "1 hour, 1 minute and 2 seconds"
```
```javascript
formatDuration(62)    // returns "1 minute and 2 seconds"
formatDuration(3662)  // returns "1 hour, 1 minute and 2 seconds"
```
```python
format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
```
```ruby
format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
```
```elixir
format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
```
```php
format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
```
```haskell
formatDuration 62     -- returns "1 minute and 2 seconds"
formatDuration 3662   -- returns "1 hour, 1 minute and 2 seconds"
```
```java
TimeFormatter.formatDuration(62)   //returns "1 minute and 2 seconds"
TimeFormatter.formatDuration(3662) //returns "1 hour, 1 minute and 2 seconds"
```
```groovy
Kata.formatDuration(62)   //returns "1 minute and 2 seconds"
Kata.formatDuration(3662) //returns "1 hour, 1 minute and 2 seconds"
```
```shell
duration 62            # echos "1 minute and 2 seconds"
duration 3662          # echos "1 hour, 1 minute and 2 seconds"
```
```julia
formatduration(62)    # returns "1 minute and 2 seconds"
formatduration(3662)  # returns "1 hour, 1 minute and 2 seconds"
```
```racket
(format-duration 62)    ; returns "1 minute and 2 seconds"
(format-duration 3662)  ; returns "1 hour, 1 minute and 2 seconds"
```
```rust
format_duration(62)    // returns "1 minute and 2 seconds"
format_duration(3662)  // returns "1 hour, 1 minute and 2 seconds"
```

**For the purpose of this Kata, a year is 365 days and a day is 24 hours.**

Note that spaces are important.


### Detailed rules

The resulting expression is made of components like `4 seconds`, `1 year`, etc.  In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (`", "`). Except the last component, which is separated by `" and "`, just like it would be written in English. 

A more significant units of time will occur before than a least significant one. Therefore, `1 second and 1 year` is not correct, but `1 year and 1 second` is.

Different components have different unit of times. So there is not repeated units like in `5 seconds and 1 second`.

A component will not appear at all if its value happens to be zero.  Hence, `1 minute and 0 seconds` is not valid, but it should be just `1 minute`.

 A unit of time must be used "as much as possible". It means that the function should not return `61 seconds`, but `1 minute and 1 second` instead.  Formally, the duration specified by  of a component must not be greater than any valid more significant unit of time.
"""

intervals = {'years': 31536000,
    'days': 86400, 
    'hours': 3600,  
    'minutes': 60,
    'seconds': 1,}
def format_duration(seconds):
    if seconds == 0:
        return 'now' 
    res = []
    for k,v in intervals.items():
        time = seconds // v
        if time:
            seconds -= time * v
            if time == 1:
                k = k.rstrip('s')
            res.append(f"{time} {k}")
    if len(res) <= 1:
        return res[0]
    else:
        return ', '.join(res[:-1]) +" and "+ res[-1]
#2021-09-20 13:19:53.538000+00:00
"""Define a function that takes one integer argument and returns logical value `true` or `false` depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

## Requirements

* You can assume you will be given an integer input.
* You can not assume that the integer will be only positive. You may be given negative numbers as well (or `0`).
* **NOTE on performance**: There are no fancy optimizations required, but still *the* most trivial solutions might time out. Numbers go up to 2^31 (or similar, depends on language version). Looping all the way up to `n`, or `n/2`, will be too slow.


## Example
```c
is_prime(1)  /* false */
is_prime(2)  /* true  */
is_prime(-1) /* false */
```
```nasm    
mov edi, 1
call is_prime    ; EAX <- 0 (false)

mov edi, 2
call is_prime    ; EAX <- 1 (true)

mov edi, -1
call is_prime    ; EAX <- 0 (false)
```
```c++
bool isPrime(5) = return true
```
```pascal
IsPrime(1) = false
IsPrime(2) = true
IsPrime(-1) = false
```
"""

from math import sqrt

def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0 or num <=1:
        return False
    for i in range(3,int(sqrt(num)+1), 2):
        if num % i == 0:
            return False
    return True
                
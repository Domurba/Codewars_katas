#2021-10-25 13:58:54.646000+00:00
"""This time we want to write calculations using functions and get the results. Let's have a look at some examples:

```javascript
seven(times(five())); // must return 35
four(plus(nine())); // must return 13
eight(minus(three())); // must return 5
six(dividedBy(two())); // must return 3
```
```haskell
seven $ times $ five   ->  35 :: Int
four $ plus $ nine     ->  13 :: Int
eight $ minus $ three  ->   5 :: Int
six $ dividedBy $ two  ->   3 :: Int
```
```ruby
seven(times(five)) # must return 35
four(plus(nine)) # must return 13
eight(minus(three)) # must return 5
six(divided_by(two)) # must return 3
```
```python
seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
```
```factor
seven multiplied-by five   ! must evaluate to 35
four plus nine             ! must evaluate to 13
eight minus three          ! must evaluate to 5
six divided-by two         ! must evaluate to 3
```

Requirements:
~~~if:ruby,python
* There must be a function for each number from 0 ("zero") to 9 ("nine")
* There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
* Each calculation consist of exactly one operation and two numbers
* The most outer function represents the left operand, the most inner function represents the right operand
* Division should be **integer division**. For example, this should return `2`, not `2.666666...`:
~~~
~~~if:factor
* There must be a word for each number from 0 ("zero") to 9 ("nine")
* There must be a word for each of the following mathematical operations: plus, minus, multiplied-by, divided-by
* Each calculation consist of exactly one operation and two numbers
* The leftmost word represents the left operand, the rightmost word represents the right operand
* Division should be **integer division**. For example, this should return `2`, not `2.666666...`:
~~~
~~~if-not:ruby,python,factor
* There must be a function for each number from 0 ("zero") to 9 ("nine")
* There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy
* Each calculation consist of exactly one operation and two numbers
* The most outer function represents the left operand, the most inner function represents the right operand
* Division should be **integer division**. For example, this should return `2`, not `2.666666...`:
~~~

```javascript
eight(dividedBy(three()));
```
```haskell
eight $ dividedBy $ three
```
```ruby
eight(divided_by(three))
```
```python
eight(divided_by(three()))
```
```factor
eight divided-by three
```"""

def zero(act=None):
    if not act: return 0
    return act(0)
def one(act=None):
    if not act: return 1
    return act(1)
def two(act=None):
    if not act: return 2
    return act(2)
def three(act=None):
    if not act: return 3
    return act(3)
def four(act=None):
    if not act: return 4
    return act(4)
def five(act=None):
    if not act: return 5
    return act(5)
def six(act=None):
    if not act: return 6
    return act(6)
def seven(act=None):
    if not act: return 7
    return act(7) 
def eight(act=None):
    if not act: return 8
    return act(8)
def nine(act=None):
    if not act: return 9
    return act(9)

def plus(y):
    return lambda x: x+y
def minus(y):
    return lambda x: x-y
def times(y):
    return lambda x: x*y
def divided_by(y):
    return lambda x: x//y
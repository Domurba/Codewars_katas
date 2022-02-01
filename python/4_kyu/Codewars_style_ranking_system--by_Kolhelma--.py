#2021-11-24 16:30:55.195000+00:00
"""Write a class called User that is used to calculate the amount that a user will progress through a ranking system similar to the one Codewars uses.  

##### Business Rules:

* A user starts at rank -8 and can progress all the way to 8.
* There is no 0 (zero) rank. The next rank after -1 is 1.
* Users will complete activities. These activities also have ranks.
* Each time the user completes a ranked activity the users rank progress is updated based off of the activity's rank
* The progress earned from the completed activity is relative to what the user's current rank is compared to the rank of the activity
* A user's rank progress starts off at zero, each time the progress reaches 100 the user's rank is upgraded to the next level
* Any remaining progress earned while in the previous rank will be applied towards the next rank's progress (we don't throw any progress away). The exception is if there is no other rank left to progress towards (Once you reach rank 8 there is no more progression). 
* A user cannot progress beyond rank 8. 
* The only acceptable range of rank values is -8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8. Any other value should raise an error. 

The progress is scored like so:

* Completing an activity that is ranked the same as that of the user's will be worth 3 points
* Completing an activity that is ranked one ranking lower than the user's will be worth 1 point
* Any activities completed that are ranking 2 levels or more lower than the user's ranking will be ignored
* Completing an activity ranked higher than the current user's rank will accelerate the rank progression. The greater the difference between rankings the more the progression will be increased. The formula is `10 * d * d` where `d` equals the difference in ranking between the activity and the user.  

##### Logic Examples:
* If a user ranked -8 completes an activity ranked -7 they will receive 10 progress
* If a user ranked -8 completes an activity ranked -6 they will receive 40 progress
* If a user ranked -8 completes an activity ranked -5 they will receive 90 progress
* If a user ranked -8 completes an activity ranked -4 they will receive 160 progress, resulting in the user being upgraded to rank -7 and having earned 60 progress towards their next rank
* If a user ranked -1 completes an activity ranked 1 they will receive 10 progress (remember, zero rank is ignored)

##### Code Usage Examples:
```javascript
var user = new User()
user.rank // => -8
user.progress // => 0
user.incProgress(-7)
user.progress // => 10
user.incProgress(-5) // will add 90 progress
user.progress # => 0 // progress is now zero
user.rank # => -7 // rank was upgraded to -7
```
```coffeescript
user = new User()
user.rank # => -8
user.progress # => 0
user.incProgress(-7)
user.progress # => 10
user.incProgress(-5) # will add 90 progress
user.progress # => 0 # progress is now zero
user.rank # => -7 # rank was upgraded to -7
```
```ruby
user = User.new
user.rank # => -8
user.progress # => 0
user.inc_progress(-7)
user.progress # => 10
user.inc_progress(-5) # will add 90 progress
user.progress # => 0 # progress is now zero
user.rank # => -7 # rank was upgraded to -7
```
```python
user = User()
user.rank # => -8
user.progress # => 0
user.inc_progress(-7)
user.progress # => 10
user.inc_progress(-5) # will add 90 progress
user.progress # => 0 # progress is now zero
user.rank # => -7 # rank was upgraded to -7
```
```java
User user = new User();
user.rank; // => -8
user.progress; // => 0
user.incProgress(-7);
user.progress; // => 10
user.incProgress(-5); // will add 90 progress
user.progress; // => 0 // progress is now zero
user.rank; // => -7 // rank was upgraded to -7
```
```haskell
rank newUser -- => -8
progress newUser -- => 0
let u2 = incProgress (-7) newUser
progress u2 -- =>  10
let u3 = incProgress (-5) u2 -- will add 90 progress
progress u3 -- => 0 -- progress is now zero
rank u3 -- => -7 -- rank was upgraded to -7
```
```csharp
User user = new User();
user.rank; // => -8
user.progress; // => 0
user.incProgress(-7);
user.progress; // => 10
user.incProgress(-5); // will add 90 progress
user.progress; // => 0 // progress is now zero
user.rank; // => -7 // rank was upgraded to -7
```

~~~if:java
**Note:** In **Java** some methods may throw an `IllegalArgumentException`.
~~~
~~~if:csharp
**Note:** In **C#** some methods may throw an `ArgumentException`.
~~~

**Note**: Codewars no longer uses this algorithm for its own ranking system. It uses a pure Math based solution that gives consistent results no matter what order a set of ranked activities are completed at. 
"""

class User:
    # index 0 == -8 >>>> index 15 == 8
    global ranks
    ranks = list(range(-8, 0)) + list(range(1, 9))
    global d
    d = {
        -8: 0,
        -7: 1,
        -6: 2,
        -5: 3,
        -4: 4,
        -3: 5,
        -2: 6,
        -1: 7,
        1: 8,
        2: 9,
        3: 10,
        4: 11,
        5: 12,
        6: 13,
        7: 14,
        8: 15,
    }

    def __init__(self):
        self.rank_index = 0
        self.rank = ranks[self.rank_index]
        self.progress = 0

    def inc_progress(self, rnk):
        print ('start rank', self.rank)
        print ('rank of kata', rnk)        
        if not rnk in d.keys():
            raise Exception("bad value")
        if self.rank < 8 and rnk in d.keys():
            if d[rnk] + 1 < d[self.rank]:
                pass
            elif d[rnk] + 1 == d[self.rank]:
                self.rank_check(1)

            elif d[rnk] == d[self.rank]:
                self.rank_check(3)
            else:
                pts = 10 * (d[rnk] - d[self.rank]) ** 2
                self.rank_check(pts)

    def rank_check(self, r):
        print ('received pts ', r)        
        self.progress += r
        print ('pts after adding' , self.progress)        
        if self.progress >= 100 and self.rank < 8:
            up, left = divmod(self.progress, 100)
            self.rank_index += up
            self.rank = ranks[self.rank_index]
            self.progress = left
        if self.rank == 8: 
            self.progress = 0
        print ('rank after check', self.rank)
        print ('pts after check' , self.progress)       
#2021-11-29 10:23:57.736000+00:00
"""MongoDB is a noSQL database which uses the concept of a document, rather than a table as in SQL. Its popularity is growing.

As in any database, you can create, read, update, and delete elements. But in constrast to SQL, when you create an element, a new field `_id` is created. This field is unique and contains some information about the time the element was created, id of the process that created it, and so on. More information can be found in the [MongoDB documentation](http://docs.mongodb.org/manual/reference/object-id/) (which you have to read in order to implement this Kata).

So let us implement the following helper which will have 2 methods:
 - one which verifies that the string is a valid Mongo ID string, and
 - one which finds the timestamp from a MongoID string

*Note:*

If you take a close look at a Codewars URL, you will notice each kata's id (the `XXX` in `http://www.codewars.com/dojo/katas/XXX/train/javascript`) is really similar to MongoDB's ids, which brings us to the conjecture that this is the database powering Codewars.


## Examples

The verification method will return `true` if an element provided is a valid Mongo string and `false` otherwise:

```javascript
Mongo.isValid('507f1f77bcf86cd799439011')  // true
Mongo.isValid('507f1f77bcf86cz799439011')  // false
Mongo.isValid('507f1f77bcf86cd79943901')   // false
Mongo.isValid('111111111111111111111111')  // true
Mongo.isValid(111111111111111111111111)    // false
Mongo.isValid('507f1f77bcf86cD799439011')  // false (we arbitrarily only allow lowercase letters)
```
```python
Mongo.is_valid('507f1f77bcf86cd799439011')  # True
Mongo.is_valid('507f1f77bcf86cz799439011')  # False
Mongo.is_valid('507f1f77bcf86cd79943901')   # False
Mongo.is_valid('111111111111111111111111')  # True
Mongo.is_valid(111111111111111111111111)    # False
Mongo.is_valid('507f1f77bcf86cD799439011')  # False (we arbitrarily only allow lowercase letters)
```
```ruby
Mongo.is_valid('507f1f77bcf86cd799439011')  # true
Mongo.is_valid('507f1f77bcf86cz799439011')  # false
Mongo.is_valid('507f1f77bcf86cd79943901')   # false
Mongo.is_valid('111111111111111111111111')  # true
Mongo.is_valid(111111111111111111111111)    # false
Mongo.is_valid('507f1f77bcf86cD799439011')  # false (we arbitrarily only allow lowercase letters)
```

The timestamp method will return a date/time object from the timestamp of the Mongo string and false otherwise:

```javascript
// Mongo.getTimestamp should return a Date object

Mongo.getTimestamp('507f1f77bcf86cd799439011')  // Wed Oct 17 2012 21:13:27 GMT-0700 (Pacific Daylight Time)
Mongo.getTimestamp('507f1f77bcf86cz799439011')  // false
Mongo.getTimestamp('507f1f77bcf86cd79943901')   // false
Mongo.getTimestamp('111111111111111111111111')  // Sun Jan 28 1979 00:25:53 GMT-0800 (Pacific Standard Time)
Mongo.getTimestamp(111111111111111111111111)    // false
```
```python
# Mongo.get_timestamp should return a datetime object

Mongo.get_timestamp('507f1f77bcf86cd799439011')  # Wed Oct 17 2012 21:13:27 GMT-0700 (Pacific Daylight Time)
Mongo.get_timestamp('507f1f77bcf86cz799439011')  # False
Mongo.get_timestamp('507f1f77bcf86cd79943901')   # False
Mongo.get_timestamp('111111111111111111111111')  # Sun Jan 28 1979 00:25:53 GMT-0800 (Pacific Standard Time)
Mongo.get_timestamp(111111111111111111111111)    # False
```
```ruby
# Mongo.get_timestamp should return a datetime object

Mongo.get_timestamp('507f1f77bcf86cd799439011')  # Wed Oct 17 2012 21:13:27 GMT-0700 (Pacific Daylight Time)
Mongo.get_timestamp('507f1f77bcf86cz799439011')  # false
Mongo.get_timestamp('507f1f77bcf86cd79943901')   # false
Mongo.get_timestamp('111111111111111111111111')  # Sun Jan 28 1979 00:25:53 GMT-0800 (Pacific Standard Time)
Mongo.get_timestamp(111111111111111111111111)    # false
```

When you will implement this correctly, you will not only get some points, but also would be able to check creation time of all the kata here :-)"""

from datetime import datetime
import pytz
import re


class Mongo:
    def is_valid(s):
        """returns True if s is a valid MongoID; otherwise False"""
        if isinstance(s, str):
            return all((len(s) == 24, re.search(r"[a-z0-9]+", s).group() == s))
        return False

    @classmethod
    def get_timestamp(cls, s):
        """if s is a MongoID, returns a datetime object for the timestamp; otherwise False"""
        if cls.is_valid(s):
            return datetime.fromtimestamp(int(s[0:8], 16))
        return False
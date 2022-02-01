#2021-09-26 12:59:39.540000+00:00
"""Scientists working internationally use metric units almost exclusively. Unless that is, they wish to crash multimillion dollars worth of equipment on Mars.

Your task is to write a simple function that takes a number of meters, and outputs it using metric prefixes.

In practice, meters are only measured in "mm" (thousandths of a meter), "cm" (hundredths of a meter), "m" (meters) and "km" (kilometers, or clicks for the US military).

For this exercise we just want units bigger than a meter, from meters up to yottameters, excluding decameters and hectometers.

All values passed in will be positive integers.
e.g.

```javascript
meters(5);
// returns "5m"

meters(51500);
// returns "51.5km"

meters(5000000);
// returns "5Mm"
```
```ruby
meters(5);
// returns "5m"

meters(51500);
// returns "51.5km"

meters(5000000);
// returns "5Mm"
```
```python
meters(5);
// returns "5m"

meters(51500);
// returns "51.5km"

meters(5000000);
// returns "5Mm"
```

```haskell
meters 5
-- returns "5m"

meters 51500
-- returns "51.5km"

meters 5000000
-- returns "5Mm"
```

See http://en.wikipedia.org/wiki/SI_prefix for a full list of prefixes
"""

def meters(x):
    if x // 10 ** 24:
        return str(x // 10 ** 21 / 1000).rstrip("0").rstrip(".") + "Ym"
    elif x // 10 ** 21:
        return str(x // 10 ** 18 / 1000).rstrip("0").rstrip(".") + "Zm"
    elif x // 10 ** 18:
        return str(x // 10 ** 15 / 1000).rstrip("0").rstrip(".") + "Em"    
    elif x // 10 ** 15:
        return str(x // 10 ** 12 / 1000).rstrip("0").rstrip(".") + "Pm" 
    elif x // 10 ** 12:
        return str(x // 10 ** 9 / 1000).rstrip("0").rstrip(".") + "Tm" 
    elif x // 10 ** 9:
        return str(x // 10 ** 6 / 1000).rstrip("0").rstrip(".") + "Gm" 
    elif x // 10 ** 6:
        return str(x // 10 ** 3 / 1000).rstrip("0").rstrip(".") + "Mm" 
    elif x // 10 ** 3:
        return str(x // 10 ** 0 / 1000).rstrip("0").rstrip(".") + "km" 
    elif x // 10 ** 0:
        return str(x // 10 ** 0).rstrip("0").rstrip(".") + "m" 

#2022-01-11 12:32:11.865000+00:00
"""Let's pretend your company just hired your friend from college and paid you a referral bonus. Awesome! To celebrate, you're taking your team out to the terrible dive bar next door and using the referral bonus to buy, and build, the largest three-dimensional beer can pyramid you can. And then probably drink those beers, because let's pretend it's Friday too. 

A beer can pyramid will square the number of cans in each level - 1 can in the top level, 4 in the second, 9 in the next, 16, 25... 

Complete the beeramid function to return the number of **complete** levels of a beer can pyramid you can make, given the parameters of: 

1) your referral bonus, and

2) the price of a beer can

For example:

```javascript
beeramid(1500, 2); // should === 12
beeramid(5000, 3); // should === 16
```
```prolog
beeramid(1500, 2, 12). % 12 levels
beeramid(5000, 3, 16). % 16 levels
```"""

def sum_sqr(n, p):
    return ((n * (n + 1) * (2 * n + 1)) / 6) * p


def beeramid(q, p):
    height, pyra = 0, 0
    while q > pyra:
        height += 1
        pyra = sum_sqr(height, p)
    if q == pyra or q < 0:
        return height
    return height - 1
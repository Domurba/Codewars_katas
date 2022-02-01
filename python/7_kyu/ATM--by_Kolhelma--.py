#2021-10-11 08:47:23.322000+00:00
"""There is enough money available on ATM in nominal value 10, 20, 50, 100, 200 and 500 dollars.

You are given money in nominal value of `n` with `1<=n<=1500`.

Try to find minimal number of notes that must be used to repay in dollars, or output <code lang="java">-1</code> if it is impossible.

Good Luck!!!"""

def solve(n):
    if n % 10 != 0:
        return -1
    bills500 = n // 500
    n -= bills500*500
    bills200 = n // 200
    n -= bills200*200
    bills100 = n // 100
    n -= bills100*100
    bills50 = n // 50
    n -= bills50*50
    bills20 = n // 20
    n -= bills20*20
    bills10 = n // 10 
    n -= bills10*10
    return bills10+bills20+bills50+bills100+bills200+bills500
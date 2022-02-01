#2021-09-21 13:14:36.393000+00:00
"""You have function `one_two` (`oneTwo` for Java) that returns 1 or 2 with 50% chance. `one_two` is already defined in a global scope and can be called everywhere.

Your goal is to create function `one_two_three` (`oneTwoThree` for Java) that returns 1, 2 or 3 with equal probability using only `one_two` function.

Do not try to cheat returning repeating non-random sequences. There is randomness test especially for this case."""

def one_two_three():
    x = one_two()
    y = one_two()  
    z = one_two()
    if x == 1 and y == 1 and z == 1:
        return 3
    if x == 2 and y == 2 and z == 2:
        return 2
    if x == 2 and y == 2 and z == 1:
        return 1
    else:
        return one_two_three()
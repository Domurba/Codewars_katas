#2021-09-20 18:14:44.195000+00:00
"""You are given a string of numbers between 0-9. Find the average of these numbers and return it as a floored whole number (ie: no decimal places) written out as a string. Eg:

"zero nine five two" -> "four"

If the string is empty or includes a number greater than 9, return "n/a"





"""

def average_string(s):
    if not s.replace(" ", ""):
        return "n/a"
    try:
        s = (
            s.replace("zero", "0")
            .replace("one", "1")
            .replace("two", "2")
            .replace("three", "3")
            .replace("four", "4")
            .replace("five", "5")
            .replace("six", "6")
            .replace("seven", "7")
            .replace("eight", "8")
            .replace("nine", "9")
            .replace(" ", "")
        )
        k = str(int(sum(int(i) for i in s) / len(s)))
        return (
            k.replace("0", "zero")
            .replace("1", "one")
            .replace("2", "two")
            .replace("3", "three")
            .replace("4", "four")
            .replace("5", "five")
            .replace("6", "six")
            .replace("7", "seven")
            .replace("8", "eight")
            .replace("9", "nine")
        )
    except:
        return "n/a"
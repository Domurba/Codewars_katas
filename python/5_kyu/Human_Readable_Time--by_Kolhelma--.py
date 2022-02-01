#2021-10-19 08:25:48.391000+00:00
"""Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (`HH:MM:SS`)

* `HH` = hours, padded to 2 digits, range: 00 - 99
* `MM` = minutes, padded to 2 digits, range: 00 - 59
* `SS` = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (`99:59:59`)

You can find some examples in the test fixtures."""

def make_readable(seconds):
    intervals = [3600, 60, 1]
    time = []
    for i in intervals:
        val, seconds = divmod(seconds, i)
        time.append(('0'+str(val))[-2:])
    return ':'.join(time)
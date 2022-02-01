#2021-11-18 12:59:29.154000+00:00
"""Time to build a crontab parser... https://en.wikipedia.org/wiki/Cron

A crontab command is made up of 5 fields in a space separated string:

```
minute: 0-59
hour: 0-23
day of month: 1-31
month: 1-12
day of week: 0-6 (0 == Sunday)
```

Each field can be a combination of the following values:

* a wildcard `*` which equates to all valid values.
* a range `1-10` which equates to all valid values between start-end inclusive.
* a step `*/2` which equates to every second value starting at 0, or 1 for day of month and month.
* a single value `2` which would be 2.
* a combination of the above separated by a `,`

Note: In the case of multiple values in a single field, the resulting values should be sorted.

Note: Steps and ranges can also be combined `1-10/2` would be every second value in the `1-10` range `1 3 5 7 9`.

For an added challenge day of week and month will both support shortened iso formats:

```
SUN MON TUE ...
JAN FEB MAR ...
```

Examples
========

`*` should output every valid value `0 1 2 3 4 5 6 ...`

`1` should output the value `1`.

`1,20,31` should output the values `1 20 31`.

`1-10` should output the values `1 2 3 4 5 6 7 8 9 10`.

`*/2` should output every second value `0 2 4 6 8 10 ...`.

`*/2` should output `1 3 5 7 9 ...` in the cases, day of month and month.

`1-10/2` should output `1 3 5 7 9`.

`*/15,3-5` should output the values `0 3 4 5 15 30 45` when applied to the minute field.

Output
======

The purpose of this kata is to take in a crontab command, and render it in a nice human readable format.

The output format should be in the format `field_name      values`. The field name should be left justified and
padded to 15 characters. The values should be a space separated string of the returned values.

For example the crontab `*/15 0 1,15 * 1-5` would have the following output:

```
minute          0 15 30 45
hour            0
day of month    1 15
month           1 2 3 4 5 6 7 8 9 10 11 12
day of week     1 2 3 4 5
```

All test cases will receive a valid crontab, there is no need to handle an incorrect number of values.

Super handy resource for playing with different values to find their outputs: https://crontab.guru/"""

from re import findall, sub, IGNORECASE
import calendar


times = {
    "minute": range(60),
    "hour": range(24),
    "day of month": range(1, 32),
    "month": range(1, 13),
    "day of week": range(7),
}
field_names = list(times)


def parse(crontab):
    final = []
    for i, v in enumerate(calendar.month_abbr[1:]):
        crontab = sub(v, str(i + 1), crontab, flags=IGNORECASE)
    weekdays = [calendar.day_abbr[-1]] + calendar.day_abbr[:-1]
    for i, v in enumerate(weekdays):
        crontab = sub(v, str(i), crontab, flags=IGNORECASE)
    for i, v in enumerate(crontab.split(" ")):
        field = field_names[i]
        field_values = times[field]
        v = v.replace("*", f"{field_values[0]}-{field_values[-1]}")
        inner = [field.ljust(14)]
        vals = []
        for item in v.split(","):
            if len(item) < 3:
                vals.append(item)
            if "-" in item:
                rang = findall(r"(\d+)-(\d+)", item)[0]
                r1 = int(rang[0])
                r2 = int(rang[1]) + 1
                range_vals = list(range(min(r1, r2), max(r1, r2)))
                if "/" not in item:
                    vals += range_vals
                else:
                    step = int(item.split("/")[-1])
                    vals += range_vals[::step]
        vals.sort(key=int)
        final.append(" ".join(inner + list(map(str, vals))))
    return "\n".join(final)
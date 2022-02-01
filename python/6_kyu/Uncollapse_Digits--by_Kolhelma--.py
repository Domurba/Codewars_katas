#2021-09-17 12:37:18.589000+00:00
"""### Task

You will be given a string of English digits "stuck" together, like this:

`"zeronineoneoneeighttwoseventhreesixfourtwofive"`

Your task is to split the string into separate digits:

`"zero nine one one eight two seven three six four two five"`


### Examples
```
"three"              -->  "three"
"eightsix"           -->  "eight six"
"fivefourseven"      -->  "five four seven"
"ninethreesixthree"  -->  "nine three six three"
"fivethreefivesixthreenineonesevenoneeight"  -->  "five three five six three nine one seven one eight"
```"""

import re
def uncollapse(digits):
    return  " ".join(re.findall("(zero|nine|one|eight|two|seven|three|six|four|two|five)", digits))
#2021-10-10 12:32:18.791000+00:00
"""Your function takes two arguments:
1. current father's age (years)
2. current age of his son (years)

Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old)."""

#!/bin/sh

dad_years_old=$1
son_years_old=$2

agee=$((2 * $2 - $1))
echo ${agee#-}
exit 
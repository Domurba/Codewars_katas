#2021-09-06 14:17:32.928000+00:00
"""Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

Example:

Input:

'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

Output:

'alpha beta gamma delta'
  
"""

import re
def remove_duplicate_words(s):
    new_s = re.sub(r"\b(\w+)( \1\b)+", r"\1", s)
    return (' '.join(dict.fromkeys(new_s.split())))
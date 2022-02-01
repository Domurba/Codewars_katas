#2021-07-09 13:49:57.584000+00:00
"""What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

```
'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
```

Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

```javascript
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
```

**Note for Go**\
For Go: Empty string slice is expected when there are no anagrams found.

"""

def anagrams(word, words):
    anagram=[]
    sword = ''.join(sorted(word))
    for element in words:
        swords = ''.join(sorted(element))
        if swords == sword:
            anagram.append(element)
    return anagram
#2021-12-14 15:34:52.841000+00:00
"""#Task:
Write a function `get_member_since` which accepts a username from someone at Codewars and returns an string containing the month and year separated by a space that they joined CodeWars.

###If you want/don't want your username to be in the tests, ask me in the discourse area. There can't be too many though because the server may time out.

#Example:

```python
>>> get_member_since('dpleshkov')
Jul 2016
>>> get_member_since('jhoffner')
Oct 2012
```

#Libraries/Recommendations:

##Python:

* `urllib.request.urlopen`: Opens up a webpage.
* `re`: The RegEx library for Python.
* `bs4`([BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc)): A tool for scraping HTML and XML.
* **Python 2 is not working for this kata. :(**

#Notes:

* Time out / server errors often happen with the test cases depending on the status of the codewars website. Try submitting your code a few times or at different hours of the day if needed.
* Feel free to voice your comments and concerns in the discourse area."""

import requests
from bs4 import BeautifulSoup

URL = "https://www.codewars.com/users/"


def get_member_since(username):
    soup = BeautifulSoup(requests.get(URL + username).text, "html.parser")
    return soup.find("b", text="Member Since:").next_sibling

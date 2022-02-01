#2021-12-13 15:08:03.388000+00:00
"""You should get and parse the html of the [codewars leaderboard page](https://www.codewars.com/users/leaderboard).

You can use `Nokogiri`(Ruby) or `BeautifulSoup`(Python) or `CheerioJS`(Javascript).

For Javascript: Return a Promise resolved with your 'Leaderboard' Object!

 ----

 #### Return a 'Leaderboard' object with a position property.
```
Leaderboard#position should contain 500 'User' objects.
Leaderboard#position[i] should return the ith ranked User(1 based index).
```

 #### Each User should have the following properties
```
User#name    # => the user's username, not their real name
User#clan    # => the user's clan, empty string if empty clan field
User#honor   # => the user's honor points as an integer
```


 #### Ex:
```
  an_alien = leaderboard.position[3]   # => #<User:0x3124da0 @name="myjinxin2015", @clan="China Changyuan", @honor=21446>
  an_alien.name                        # => "myjinxin2015"
  an_alien.clan                        # => "China Changyuan"
  an_alien.honor                       # => 21446
  
```
"""

from bs4 import BeautifulSoup
import requests

class Leaderboard():
    position = {}


class User:
    def __init__(self, name, honor, clan =''):
        self.name = name
        self.clan = clan
        self.honor = honor

def solution():
    URL = "https://www.codewars.com/users/leaderboard"
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, "html.parser")
    results = soup.find("div", class_="leaderboard p-0").find_all("tr")
    leaderboard = Leaderboard()
    for n in range(1, 501):
        row = results[n].find_all("td")
        name = row[1].find("a").get_text() 
        rank = int(row[0].get_text()[1:])
        honor = int(row[3].get_text().replace(",", ""))
        clan = row[2].get_text()
        usr = User(name, honor, clan)
        leaderboard.position[rank] = usr
    return leaderboard
#2021-12-14 19:42:46.116000+00:00
"""Get the list of integers for Codewars Leaderboard score (aka Honor) in descending order

```
Note:
if it was the bad timing, the data could be updated during your test cases.
Try several times if you had such experience.
```
"""

from bs4 import BeautifulSoup
import requests
        
def get_leaderboard_honor():
    URL = "https://www.codewars.com/users/leaderboard"
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, "html.parser")
    results = soup.find("div", class_="leaderboard p-0").find_all("tr")
    ls = []
    for n in range(1, 501):
        row = results[n].find_all("td")
        honor = int(row[3].get_text().replace(",", ""))
        ls.append(honor)
    return ls

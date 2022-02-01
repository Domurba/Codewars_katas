#2021-12-14 20:04:39.662000+00:00
"""Get the list of integers for 'totalAuthored' and 'totalCompleted' of the ```n```th ranker at Codewars Leaderboard. 

```(1 <= n <= 500)```

See Example Test Cases for the expected data format.

(Note 1 : Mind the title of this kata as well as [https://dev.codewars.com/](https://dev.codewars.com/) )
 
(Note 2 : It is recommended to finish  [Codewars Leaderboard](https://www.codewars.com/kata/codewars-leaderboard/) before this kata. )

"""

from bs4 import BeautifulSoup
import requests


def all_names():
    URL = "https://www.codewars.com/users/leaderboard"
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, "html.parser")
    results = soup.find("div", class_="leaderboard p-0").find_all("tr")
    ls = ["placeholder"]
    for n in range(1, 501):
        row = results[n].find_all("td")
        name = row[1].find("a").get_text()
        ls.append(name)
    return ls


ls = all_names()


def get_codeChallenges(n):
    usr = ls[n]
    info = requests.get(f"https://www.codewars.com/api/v1/users/{usr}")
    return list(info.json()["codeChallenges"].values())
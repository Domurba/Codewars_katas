#2021-12-16 13:35:58.196000+00:00
"""# Scraping Wikipedia Links From Wikipedia Articles


You will create a function that accepts the url of a Wikipedia article as an argument.  This function will return a dictionary of keys as titles of articles (given by the title attribute of anchor tags), and values as URLs of articles.  The dictionary will only contain items that are links to other Wikipedia articles.

You will be scraping only through the div with the id "bodyContent" to do this (the content of the article on the webpage).

The values of the dictionary will be full links, not relative links:

e.g. ```'https://en.wikipedia.org/wiki/Easter_Island'``` as opposed to ```'/wiki/Easter_Island'```

<span style="color:#FF6969; font-weight:bold;">Anchor tags with links to images, help pages, categories of articles, special pages, etc will not be present in the returned dictionary; only true Wikipedia articles will be present.  This means any article that has an href in the form of /wiki/ followed by any of the strings in the following list are not to be included.</span>
```
Namespaces not to be included: 
["User:", "Wikipedia:", "WP:", "Project:", "WT:", "Project_talk", "Wikipedia_talk:",
"Image:", "Image_talk:","File:", "MediaWiki:", "Template:", "Help:", "Category:",
"Portal:", "Draft:", "TimedText:", "Module:", "Special:", "Template_talk:", "Talk:",
"File:", "File_talk:"]
```

I've found that occasionally, the random Wikipedia article generator gives an article that is too long/has too many anchor tags in it, meaning your code will inevitably time out.  If that is the case, try runnning it once or twice more."""

import requests
from bs4 import BeautifulSoup


def wikiscraping(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    body = soup.find("div", id="bodyContent")
    links = body.find_all("a", href=True, title=True)
    return {
        link["title"]: "https://en.wikipedia.org" + link["href"]
        for link in links
        if (":" not in link["href"] or "/wiki/%3F:" in link["href"]) and "wiki" in link["href"]
    }
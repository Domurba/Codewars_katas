#2021-10-26 12:54:37.047000+00:00
"""Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
```ruby
domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
```
```python
domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
```
```javascript
domainName("http://github.com/carbonfive/raygun") == "github" 
domainName("http://www.zombie-bites.com") == "zombie-bites"
domainName("https://www.cnet.com") == "cnet"
```"""

import regex
def domain_name(url):
    if not url: return ''
    return regex.findall(r'(?:https?://)?(?:www\.)?(\w*-?\w*)\.', url)[0]
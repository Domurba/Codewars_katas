#2021-08-22 14:32:13.517000+00:00
"""You are given a table named repositories, format as below:

** repositories table schema **
* project
* commits
* contributors
* address

The table shows project names of major cryptocurrencies, their numbers of commits and contributors and also a random donation address ( not linked in any way :) ).

Your job is to split out the letters and numbers from the address provided, and return a table in the following format:

** output table schema **
* project
* letters
* numbers

Case should be maintained."""

select project, 
regexp_replace(address,'[1-9]','','g') as letters,
regexp_replace(address,'[a-z]','','ig') as numbers
from repositories;
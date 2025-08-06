# In this program we use dot(.) regex and how meaning of that in regx

# Search method give us object. groups method gives us strings.

import re # importing  regex library

country_name = "Bangladesh"

match = re.search(".",country_name) # In search() method we can pass three parameter, first one is regx , second one where, and last one optional flag

print(match)

match = re.search("B.n",country_name) #B.n means one charecter betweeen B and n.
print(match)

match = re.search("B.n....",country_name)   # B.n.... means one character between B and n and 4 character after n.
print(match)

match = re.search(".......",country_name)   # ....... means match 7 character.
print(match)

check = match.group()

print(type(check))
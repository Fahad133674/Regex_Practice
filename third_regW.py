# Here we see that \w meaning in regx

import re

var = "Bangladesh is our homeland"

match = re.search("o\w\w",var) # \w meaning only latter and digit
print(match) #match with "our"

match = re.search("B\w+h",var) # \w+ meaning one or many
print(match)    #match with Bangladesh
print(match.group())
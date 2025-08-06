# Here I understand about the \d regex we use r that define that row string and treat \  a literal character, not as an escape.

import re

text = "Phone number: 01800000000"

match = re.search(r"\d+",text)
print(match.group())


text = "Hourse number is 5 ,Phone number: 01800000000"

match = re.search(r"\d+",text)
print(match.group())    # here only print 5, beacause it come first

# how we find phone number?
text = "Hourse number is 5 ,Phone number: 01800000000"

match = re.search(r"\d{11}",text)    # \d{11} meaning that we want exect 11 number, {} using that we can specify that how many we want. 
print(match.group())

# If the number content space again give wrong answer how we solve that


text = "Hourse number is 5 ,Phone number: 018 00000000"

match = re.search(r"\d{3}\s*\d{8}",text)
print(match.group()) 


# If multiple phone number exist, how can we find them?

text = "Hourse number is 5 ,Phone number: 018 00000000, 018 00000001,018 00000002"

match = re.search(r"\d{3}\s*\d{8}",text)
print(match.group()) 

print("This method not work")

# so we use findall() method , it returns list of the all findings.

text = "Hourse number is 5 ,Phone number: 018 00000000, 018 00000001,018 00000002"

match = re.findall(r"\d{3}\s*\d{8}",text) 
print(match) 
print(type(match))

print("This method work")
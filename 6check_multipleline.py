#   Here you see how apply regx in multiple line

import re

with open("file.txt","r") as f:
    text = f.read()

print(text)
# ? makes a option optional..
check = re.findall(r"^.*?$",text)
print(check)




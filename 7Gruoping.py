# here we see the use of () grouping in regx

import re

text = "<li>Tamim</li><li>Rahim</li><li>Karim</li><li>THor</li><li>Hela</li><li>locki</li>"

check = re.findall(r"<li>(.*?)</li>",text)

print(check)
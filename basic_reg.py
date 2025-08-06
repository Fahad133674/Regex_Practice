import re
s = "Afganistan, America,Bangladesh,Canada,Denmark,England,Greenland,Iceland,Netherlands, New Zealand,Sweden,Switzerland"
land = re.findall("(\w+lands*)",s) #check that word ends with lands or land
print(land)
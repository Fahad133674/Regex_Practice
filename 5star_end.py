# Here we see about the ^ and $ sign use. ^ means start with and $ means endswtih
# If we want ignore case sensitivity we use flag like I or IGNORECASE
import re

var = "Bangladesh is an independent country"

check = re.findall(r"english",var)

print(check)

# use of ^
check = re.findall(r"^Bangladesh",var)
print(check)

# use of $

check = re.findall(r"country$",var)
print(check)


# ignore flag use
print("check ignorecase\n")
check = re.findall(r'^bangladesh',var,re.I)
print(check)


check = re.findall(r'^bangladesh',var,re.IGNORECASE)
print(check)

import re

string="python is easy language"

match=re.search('\Apython',string)

print(match)
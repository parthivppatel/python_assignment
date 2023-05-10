import re

string='abc 12\ de 23 \n f45 6'

replace=''

new_string=re.sub(r'\s',replace,string,2)
print(new_string)

new_string2=re.subn(r'\s',replace,string,2)
print(new_string2)
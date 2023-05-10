from re import finditer

string="try to earn while you learn"

it=finditer("earn",string)
for i in it:
    print(i.span())
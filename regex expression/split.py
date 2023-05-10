from re import split

string="Flat is better than nested"
words=split(r' ',string)
print(words)

st2="twelve 12 eighty 80"
result=split("\d+",st2,1)
print(result)
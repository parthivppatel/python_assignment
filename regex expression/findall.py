import re

string="ram ram jay raja ram"

obj=re.findall("ram",string)
print(obj)

st2="hello i am parthiv"
obj2=re.findall("parthiv",st2)
print(obj2)

st3=re.findall(r"\w+","Fly 12 in the 16 sky.")
print(st3)

pattern='\d+'
st4="hello 12 and 13"
result=re.findall(pattern,st4)
print(result)
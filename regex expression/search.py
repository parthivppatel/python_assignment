from re import search

string="hello i am parthiv patel"

obj=search("parthiv",string)

print(obj,obj.start(),obj.end(),obj.group())
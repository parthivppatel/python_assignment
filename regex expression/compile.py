from re import *

pattern=compile(r'[aeiou]')

string="flat is better than nested"
words=split(r' ',string)

for word in words:
    print(word,pattern.match(word))


for word in words:
    print(word,pattern.search(word))

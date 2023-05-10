from re import match 

strings=["Welcome to TutorialsTeacher", "weather forecast",
"Winston Churchill","W.G.Grace","Wonders of India","Water park"]

for string in strings:
   obj = match("W[a-z]",string)
   print(obj)
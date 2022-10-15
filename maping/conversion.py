# Convert all float digits into integer using built in function from given list.

def conversion(ls):
     return round(ls)

ls=[51.5,0.5,2.4,3.5,3.6]
a=map(conversion,ls)
print(list(a))


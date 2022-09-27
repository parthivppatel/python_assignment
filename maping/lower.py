# Print all string in lower case from given tuple
def lo(a):
    return a.lower() 
loop=int(input("enter the no of elements in list: "))

i=0
myls=[]
while(i<loop):
   num=input("enter the elements of list: ")
   myls.append(num)
   i=i+1

a=map(lo,myls)
print(tuple(a))
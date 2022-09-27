# Triple all the numbers given in list

def triple(a):
    return a*a*a 
loop=int(input("enter the no of elements in list: "))

i=0
myls=[]
while(i<loop):
   num=input("enter the elements of list: ")
   myls.append(int(num))
   i=i+1

a=map(triple,myls)
print(list(a))

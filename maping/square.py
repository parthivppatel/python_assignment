# Print square root of numbers given in list

def square(a):
    return a*a 
loop=int(input("enter the no of elements in list: "))

i=0
myls=[]
while(i<loop):
   num=input("enter the elements of list: ")
   myls.append(int(num))
   i=i+1

a=map(square,myls)
print(list(a))
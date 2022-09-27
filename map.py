# Triple all the numbers given in list

# def triple(a):
#     return a*a*a 
# loop=int(input("enter the no of elements in list: "))

# i=0
# myls=[]
# while(i<loop):
#    num=input("enter the elements of list: ")
#    myls.append(int(num))
#    i=i+1

# a=map(triple,myls)
# print(list(a))

# Separate even odd number from given list
mydict={"even":[],"odd":[]}
def seprate(a):
    
    if(a%2==0):
       mydict["even"].append(a)  
    else:
       mydict["odd"].append(a)  
    return 0 
loop=int(input("enter the no of elements in list: "))

i=0
myls=[]
while(i<loop):
   num=input("enter the elements of list: ")
   myls.append(int(num))
   i=i+1

a=map(seprate,myls)
tuple(a)
print(mydict)
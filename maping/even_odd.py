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

a=list(map(seprate,myls))
print(mydict)
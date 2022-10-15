# Add ‘@gmail.com’ to all the values of given dictionary and convert it to lower case.

from ast import Store


dictionary={"1":"PARTHIV"
            ,"2":"SURAJ",
            "3":"VRAJENDRA"}

a=dictionary.values()
ls=list(a)
ls2=[]
for i in ls:
    temp=i.lower()
    # Store=temp,"@g,ail.cp,"
    ls2.append(temp)

# for i in ls:
#     i.lower()
#     print(i)
    # print(ls[i])

print(ls2)
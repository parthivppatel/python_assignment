# Add ‘@gmail.com’ to all the values of given dictionary and convert it to lower case.

dictionary={"1":"PARTHIV"
            ,"2":"SURAJ",
            "3":"VRAJENDRA"}

ls2 = list(map(lambda x : x.lower()+"@gmail.com", dictionary.values()))
ls3=list(map(lambda x:x[0]+"_"+ x[1]+"*",dictionary.items()))

print(ls2)
print(ls3)
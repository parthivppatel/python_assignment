# Using filter function, filter the even numbers so that only odd numbers are passed to the new list.

def even(num):
    if(num%2==0):
        return True
    return False

ls=[1,2,3,4]
a=filter(even,ls)
even=(list(a))

odd=[]
for i in ls:
    if(i not in even):
        odd.append(i)

print(even)
print(odd)

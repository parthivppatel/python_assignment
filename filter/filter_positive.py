# This time using filter() and list() functions filter all the positive integers in the string.

def positive(num):
    num=int(num)
    if num>0:
        return True
    return False

ls=["10","20","-30","-40"]
a=filter(positive,ls)
print(list(a))

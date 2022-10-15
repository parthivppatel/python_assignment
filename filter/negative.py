# Using filter() function filter the list so that only negative numbers are left.

def positive(num):
    if num>0:
        return False
    return True

ls=[10,20,-10,-220]

a=filter(positive,ls)
print(list(a))
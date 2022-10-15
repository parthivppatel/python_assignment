# Eliminate dustlicate letter from given string
        
def duplicate(name):
    st=""

    for i in name:
        if i not in st:
           st=st+i
    
    return st

a=map(duplicate,["abcdeedcba","hello"])
print(list(a))

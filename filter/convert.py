# Convert a number to positive if it's negative in the list. Only pass those that are converted from negative
#  to positive to the new list.[Try using map inside filter]
 
def convert(num):
    if(num<0):
        return -(num)
    return True

ls=[10,-20,40,-30]
a=filter(convert,map(convert,ls))
print(list(a))
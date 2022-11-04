# Convert a number to positive if it's negative in the list. Only pass those that are converted from negative
#  to positive to the new list.[Try using map inside filter]
 
def convert(num):
    return -(num)

ls=[10,-20,40,-30]
a=filter(lambda x: x>=0,map(convert,ls))
print(list(a))
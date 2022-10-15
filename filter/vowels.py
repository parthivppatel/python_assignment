# Using filter() and list() functions and .lower() method filter all the vowels in a given string.

def vowels(str):
    if(str=='a' or str=='e' or str=='i' or str=='o' or str=='u'):
        return True

st="DHEJBAAEE"
a=filter(vowels,st.lower())
print(list(a))
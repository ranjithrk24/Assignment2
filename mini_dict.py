dict1={}
key='a'
for i in range(26):
    dict1[chr(ord(key)+i)]=ord(key)+i
print(dict1)
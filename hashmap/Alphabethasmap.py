s="azyxyyaaaa"
q=["d","a","y","u"]

hashmap=[0]*27

for k in s:
    ascii=ord(k)
    index=ascii-97
    hashmap[index]+=1

for k in q:
    ascii = ord(k)
    index=ascii-97
    print(hashmap[index])
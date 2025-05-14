s=input("enter a name:")
q=["a","e","i","o","u"]

hashmap=[0]*27

m=0
for k in s:
    ascii =ord(k)
    index=ascii-97
    hashmap[index]+=1

for k in q:
    ascii =ord(k)
    index =ascii-97
    print(f"vowels of {k}",hashmap[index])
   
    m=m+hashmap[index]
    
print("The total vowels are",m)
n =[5,3,3,1,2,7,5,10]
m=[10,111,67,5,3,1]

hash_map=[0]*11
for s in n:
    hash_map[s]+=1

for k in m:
    if k>10 or k<1:
        print("not")
    else:
         print(hash_map[k])

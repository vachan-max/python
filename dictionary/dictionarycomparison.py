n =[5,3,3,1,2,7,5,10]
m=[10,111,67,5,3,1]
frequency={}
for i in n:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
for s in m:
    if s in frequency:
         frequency[s]+=1
    else:
        frequency[s]=1
        print(f"Frequency of {s}: {frequency[s]}")
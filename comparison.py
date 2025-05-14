n =[5,3,3,1,2,7,5,10]
m=[10,111,67,5,3,1]
for i in n:
    count=0
    for j in m:
        if i==j:
            count+=1
    print(f"count of {i}is{count}")

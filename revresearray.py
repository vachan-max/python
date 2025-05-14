num=[3,2,6,4,5,6,7,5]
l=0
r=len(num)-1

while l<r:
     num[l],num[r]=num[r],num[l]
     l+=1
     r-=1

print(num)
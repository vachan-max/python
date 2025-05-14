num=[3,1,7,6,5,3,9,0,0]

def sum(l,r,num):
    if l>=r:
        return
    num[l],num[r]=num[r],num[l]
    sum(l+1,r-1,num)
  
sum(0,len(num)-1,num)
print(num)

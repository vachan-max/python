n=153
temp=n
result=0
nod = len(str(n))
while n>0:
    last_digit = n%10
    result = result+last_digit**nod
    n=n//10

if result == temp:
    print("It is an armstrong number",result)
else:
    print("It is not an armstrong Number",result)

   

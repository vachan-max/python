num = 121
n=num
result =0
count =0
while num>0:
    count+=1
    last_digit = num%10
    result=(result*10)+last_digit
    num = num//10
   
if result==n:
    print("Palindrome",result)
else:
    print("It is not palindrome",result)
print(count)
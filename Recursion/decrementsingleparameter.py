def sum(n):
    if n==1:
        return 1
    sum(n-1)
    print(n)

sum(6)
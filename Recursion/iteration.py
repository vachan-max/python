def num(n,i):
    if i>n:
        return
    print(i)
    num(n,i+1)

num(5,1)
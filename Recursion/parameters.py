# Head up approach
def name(n):
    if n==0:
        return
    print("value")
    name(n-1)

name(5)


#tail down approach

def name(n):
    if n==0:
        return
    name(n-1)
    print("value")

name(5)
count=0
def name():
    global count
    if count==4:
        return
    print("value")
    count+=1
    name()

name()
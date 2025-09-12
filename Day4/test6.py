mylist = [1,2,3,4,5,6,7,8,9,10]
def mywhile():
    i = 0
    while i < len(mylist):
        if mylist[i] % 2 == 0:
            print(mylist[i])
        i += 1

def myfor():
    for i in mylist:
        if i % 2 == 0:
            print(i)

# mywhile()
# myfor()
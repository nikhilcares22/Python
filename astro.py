item=int(input("Enter the integer n - "))
m=int(input("Enter the integer b(1 or 0) - "))
x=True
while(x):
    if m==1:
        b=True
        x=False
    elif m==0:
        b=False
        x = False
    else:
        x = True
        m = int(input("please enter only 1 or 0"))
        continue


if b==True:
    for i in range(1, item + 1):
        for j in range(i):
            print("*", end='')
        print()
elif b==False:
    for i in range(1, item + 1):
        for j in range(1, item + 2 - i):
            print("*", end="")
        print()

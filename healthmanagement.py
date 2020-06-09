def getdate():
    import datetime
    return datetime.datetime.now()

def take(a):
    k='y'
    while k=='y':
        if a == 1:  # Rohan
            c = int(input("Enter 1 for exercise and 2 for food \n"))
            if c == 1:
                x = input("Type your data now\n")
                with open("Rohan_ex.txt", "a") as f:  # appendmode
                    f.write(str(getdate()) + ":" + x + "\n")
                    print("successfully written")
            elif (c == 2):
                x = input("Type your data now\n")
                with open("Rohan_food.txt", "a") as f:  # appendmode
                    f.write(str(getdate()) + ":" + x + "\n")
                    print("successfully written")

        elif a == 2:  # This is for Rahul
            c = int(input("Enter 1 for exercise and 2 for food \n"))
            if c == 1:
                x = input("Type your data now\n")
                with open("Rahul_ex.txt", "a") as f:  # appendmode
                    f.write(str(getdate()) + ":" + x + "\n")
                    print("successfully written")
            elif (c == 2):
                x = input("Type your data now\n")
                with open("Rahul_food.txt", "a") as f:  # appendmode
                    f.write(str(getdate()) + ":" + x + "\n")
                    print("successfully written")

        elif a == 3:  # this is for nikhil
            c = int(input("Enter 1 for exercise and 2 for food \n"))
            if c == 1:
                x = input("Type your data now\n")
                with open("Nikhil_ex.txt", "a") as f:  # appendmode
                    f.write(str(getdate()) + ":" + x + "\n")
                    print("successfully written")
            elif (c == 2):
                x = input("Type your data now\n")
                with open("Nikhil_food.txt", "a") as f:  # appendmode
                    f.write(str(getdate()) + ":" + x + "\n")
                    print("successfully written")
        k=input("Enter y to add  more and n to not\n")
        if k=='y':
            a=int(input("Enter 1 for Rohan ,2 for Rahul & 3 for Nikhil\n"))
        else:
            print("thank u")

def retrieve(a):        #To retrieve data
    if a==1:    #Rohan
        c = int(input("Enter 1 for exercise and 2 for food \n"))
        if c==1:
            with open("Rohan_ex.txt") as f: #Read mode as default
                print(f.read())
        elif c==2:
            with open("Rohan_food.txt") as f:  # Read mode as default
                print(f.read())
    elif a==2:  #rahul
        c = int(input("Enter 1 for exercise and 2 for food \n"))
        if c == 1:
            with open("Rahul_ex.txt") as f:  # Read mode as default
                print(f.read())
        elif c == 2:
            with open("Rahul_food.txt") as f:  # Read mode as default
                print(f.read())

    elif a==3:  #Nikhil
        c = int(input("Enter 1 for exercise and 2 for food \n"))
        if c == 1:
            with open("Nikhil_ex.txt") as f:  # Read mode as default
                print(f.read())
        elif c == 2:
            with open("Nikhil_food.txt") as f:  # Read mode as default
                print(f.read())


print("Welcome to health management system")
a = int(input("Enter 1 to log & 2 to retrieve\n"))
if a==1:
    t=int(input("Enter 1 for Rohan ,2 for Rahul & 3 for Nikhil\n"))
    take(t)
elif a==2:
    t = int(input("Enter 1 for Rohan ,2 for Rahul  & 3 for Nikhil\n"))
    retrieve(t)
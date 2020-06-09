a = int(input("Welcome to guess the number\nPlease enter your choice between 1-30 \n"))
c = 4
n = 24 #the answer
while c>0:
        if a<n:
             print("Your number is smaller than the answer")
        elif a>n:
            print("Your number is bigger than the answer")
        else:

            break
        c -= 1
        print("You have  ",c+1," chances left")
        a=int(input("Enter the number again \n"))

if a==n:
    print("You win!")
else:
    print("You Lost!")
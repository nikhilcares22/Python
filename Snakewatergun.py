import random
list_1 = ['S','G','W']

print("Welcome to Snake, Water , Gun")

count =10
pc=0
you=0
while count>0:
    ch_1 = random.choice(list_1)
    a = input("Enter your choice- S for Snake, W for Water & G for Gun\n").capitalize()
    if a=='G':
        if ch_1=='W':
            #print("you Lose!")
            print(f"your choice is {a} & pc's choice is {ch_1} so you Lost!")
            pc=pc+1
            print(f"Your Score is {you} & pc's score is {pc}")
        elif ch_1=='S':
            #print("you Win!")
            print(f"your choice is {a} & pc's choice is {ch_1} so you Win!")
            you=you+1
            print(f"Your Score is {you} & pc's score is {pc}")
        else:
            #print("Draw")
            print(f"your choice is {a} & pc's choice is {ch_1} so its a Draw")
            print(f"Your Score is {you} & pc's score is {pc}")
        count=count-1


    elif a=='S':
        if ch_1=='W':
            #print("you Win!")
            print(f"your choice is {a} & pc's choice is {ch_1} so you Win!")
            you=you+1
            print(f"Your Score is {you} & pc's score is {pc}")
        elif ch_1=='G':
            #print("you Lose!")
            print(f"your choice is {a} & pc's choice is {ch_1} so you Lost!")
            pc=pc+1
            print(f"Your Score is {you} & pc's score is {pc}")
        else:
            #print("Draw")
            print(f"your choice is {a} & pc's choice is {ch_1} so its a Draw")
            print(f"Your Score is {you} & pc's score is {pc}")
        count=count-1

    elif a=='W':
        if ch_1=='S':
            #print("you Lose!")
            print(f"your choice is {a} & pc's choice is {ch_1} so you Lost!")
            pc=pc+1
            print(f"Your Score is {you} & pc's score is {pc}")
        elif ch_1=='G':
            #print("you Win!")
            print(f"your choice is {a} & pc's choice is {ch_1} so you Win!")
            you=you+1
            print(f"Your Score is {you} & pc's score is {pc}")
        else:
            #print("Draw")
            print(f"your choice is {a} & pc's choice is {ch_1} so its a Draw")
            print(f"Your Score is {you} & pc's score is {pc}")
        count=count-1

    else:
        print("Error")
        continue
print("\n")
if pc>you:
    print("You lost")
elif you>pc:
    print("You Win")
else:
    print("Its a Draw")

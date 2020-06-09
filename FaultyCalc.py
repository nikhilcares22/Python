quit='y'
while (quit=='y'):
    a = input("Enter one of these operator (/ * + -) \n")
    b = int(input("Enter first value\n"))
    c = int(input("Enter second value\n"))

    if a == ('/'):
        if b == 56 and c == 6:
            print("the result is ", 4)
        else:
            print("the result is ", b / c)

    elif a == ('*'):
        if (b == 45 and c == 3) or (b == 3 and c == 45):
            print("the result is ", 555)
        else:
            print("the result is ", b * c)
    elif a == ('+'):
        if (b == 56 and c == 9) or (b == 9 and c == 56):
            print("the result is ", 77)
        else:
            print("the result is ", b + c)
    elif a == ('-'):
        print("the result is ", b - c)
    else:
        print("Error")
    quit =input("Enter y to continue and n to exit")

print("Thank you for using calculator")


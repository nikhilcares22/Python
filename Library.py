#########MINI-PROJECT############
class Library:
    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.lend_dict={}

    def display_book(self):
        print(f"We have the following books in our library {self.name}")
        for book in self.booklist:
            print(book)
    def lend_book(self,user,book):
        if book not in self.lend_dict.keys():
            self.lend_dict.update({book:user})
            print("Success you can take the book now")
        else:
            print(f"The book has already being used by {self.lend_dict[book]}")
    def add_book(self,book):
        self.booklist.append(book)
        print("The book has been added")
    def return_book(self,book):
        self.lend_dict.pop(book)
if __name__ == '__main__':
    a=Library(["Harry Potter","Rich Daddy Poor Daddy","The parasite","The lord of the rings"],"Nikhil ")
    while(True):
        print(f"Welcome to the {a.name} Library")
        print("Enter your choice to continue")
        print("1 for display books")
        print("2 for lend a book")
        print("3 to add a book")
        print("4 to return a book")
        user_choice=input()
        if user_choice not in ["1","2","3","4"]:
            print("Enter a valid input")
            continue
        else:
            user_choice=int(user_choice)

        if user_choice==1:
            a.display_book()
        elif user_choice==2:
            book=input("Enter the name of the book")
            user=input("Enter your name")
            a.lend_book(user,book)
        elif user_choice==3:
            book=input("Enter the name of the book you want to add")
            a.add_book(book)
        elif user_choice==4:
            book=input("Enter the name of the book you want to return")
            a.return_book(book)
        else:
            print("Invalid Entry")

        user_choice2=input("Enter q to quit or c to continue")
        while (user_choice2 !='c' and user_choice2 != 'q'):
            user_choice2=input("Enter a valid input")
            if user_choice2=='c':
                continue
            elif user_choice2=='q':
                exit()

def searcher():
    book="This is my book Nikhil Sharma"
    import time
    time.sleep(4)
    #a task taking 4 seconds
    while True:
        text=(yield)
        if text in book:
            print("in the book")
        else:
            print("not in the book")
search=searcher()
print("search started ")
next(search)
input("press any key")
search.send("This")
input("press any key")
search.send("His")
input("press any key")
search.send("Nikhil")
search.close()
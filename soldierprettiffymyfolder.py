import os
def soldier(path,file,format):
    os.chdir(path)
    i=1
    files=os.listdir(path)
    with open (file) as f:
        filelist=f.read().split("\n")   #not to be changed

    for file in files:
        if file not in filelist:
            os.rename(file,file.capitalize())
        if os.path.splitext(file)[1]==format:   #returns a tuple with 1 as its extension
            os.rename(file,f"{i}{format}")
            i+=1

soldier(r"C:\Users\94178\Desktop\New folder (2)",
        r"C:\Users\94178\Desktop\ext.txt",".jpg")

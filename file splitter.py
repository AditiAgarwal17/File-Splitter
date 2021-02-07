import os
#from tkinter import *
#from tkinter.messagebox import showinfo
file_name = input("Enter file name:")
n = int(input("Enter number of partitions:"))
x=open(file_name,"rb")
y=x.read()
chars=len(y)//n
def splitter(y,chars):
    global file_name
    global n
    for i in range(n):
        a=open("a"+str(i+1)+".txt","wb")
        a.write(y[:chars])
        y = y[chars:]
        if(len(y)<chars):
            a.write(y)
        a.close()
    #showinfo("result", "File Successfully Split")

def joiner(y):
    global file_name
    global n
    for i in range(n):
        a = open("a" + str(i + 1) + ".txt", "rb")
        a=a.read()
        joinedFile=open("JoinedFile.txt","ab")
        joinedFile.write(a)
    #showinfo("result", "File Successfully Joined")
#def window():
    #global file_name
    #global n
    #root=Tk()
    #root.title("File Splitter!")
    #root.geometry("600x400")
    #root.resizable(0,0)

    #l1 = Label(root, text="Enter File Name:", font=("",11), bg="#091e42", fg="white")
    #l1.place(x=150,y=50)
    #e1 = Entry(root, font=("", 11))
    #e1.place(x=340,y=50,width=120)
    #l2 = Label(root, text="Enter number of partitions:", font=("", 11), bg="#091e42", fg="white")
    #l2.place(x=150,y=100)
    #e2 = Entry(root, font=("", 11))
    #e2.place(x=340,y=100,width=120)
    #b1=Button(root,text="Split",font=("",20),command=splitter)
    #b1.place(x=200, y=350, width=120, height=40)
    #b2 = Button(root, text="Join",font=("",20),command=joiner)
    #b2.place(x=350, y=350, width=120, height=40)
    #root.mainloop()

#window()


splitter(y,chars)
joiner(y)
x.close()


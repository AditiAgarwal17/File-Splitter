import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


def select_files():
    #Function to select files from the Explorer
    global filenames
    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=(
            ('text files', '*.txt'),
            ('All files', '*.*')
        ))

    showinfo(
        title='Selected Files',
        message=filenames
    )
def splitter():
    #Function to split the chosen file into n number of partitions
    global  e1
    global e2
    global filenames
    file_name = ''.join(filenames)
    n = int(e1.get())
    ext=e2.get()
    x = open(file_name, "rb")
    y = x.read()
    chars = len(y) // n
    for i in range(n):
        a = open("a" + str(i + 1) + ext, "wb")
        a.write(y[:chars])
        y = y[chars:]
        if (len(y) < chars):
            a.write(y)
        a.close()
    showinfo("result", "File Successfully Split")


def joiner():
    #Function to join the selected files to a single file
    global filenames
    global e2
    ext = e2.get()
    data = ';'.join(filenames)
    data=data+";"+ext
    file_name = list(data.split(";"))
    files = file_name[:-1]
    joined_file = open("joined_file" + ext, "wb")

    for fl in files:
        a = open(fl, "rb")
        joined_file.write(a.read())
        a.close()
    joined_file.close()
    showinfo("result", "File Successfully Joined")


def window():
    global filenames
    global n
    global  e1
    global e2
    root = Tk()
    root.title('File Splitter!')
    root.geometry('600x400')
    root.resizable(0, 0)

    open_button = ttk.Button(root,text='Select Files',command=select_files)
    open_button.pack(expand=True)
    l1 = Label(root, text="Enter number of partitions:", font=("", 11), bg="#091e42", fg="white")
    l1.place(x=150, y=80)
    e1 = Entry(root, font=("", 11))
    e1.place(x=340, y=80, width=120)

    l2 = Label(root, text="Desired File Extension:", font=("", 11), bg="#091e42", fg="white")
    l2.place(x=150, y=140)
    e2 = Entry(root, font=("", 11))
    e2.place(x=340, y=140, width=120)


    b1 = Button(root, text="Split", font=("", 20), command=splitter)
    b1.place(x=150, y=320, width=120, height=40)
    b2 = Button(root, text="Join", font=("", 20), command=joiner)
    b2.place(x=350, y=320, width=120, height=40)
    root.mainloop()

window()

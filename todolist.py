from tkinter import *
from tkinter import messagebox
from datetime import datetime

root = Tk()
root.geometry('900x400')
root.title("TO DO LIST -By error_terminator")
root.config(background="red")

Lb = Label(root, text="Enter the Highest Priority Tasks Below ", fg='white', bg='black', height=1, width=40,
           justify="left")
Lb7 = Label(root, text="Date", fg='white', bg='black', height=1, width=10, justify="left")
Lb8 = Label(root, text="Task", fg='white', bg='black', height=1, width=10, justify="left")
Lb2 = Label(root, text="Task 1", fg='white', bg='black', height=1, width=15, justify="left")
Lb3 = Label(root, text="Task 2", fg='white', bg='black', height=1, width=15, justify="left")
Lb4 = Label(root, text="Task 3", fg='white', bg='black', height=1, width=15, justify="left")
Lb5 = Label(root, text="Task 4", fg='white', bg='black', height=1, width=15, justify="left")
Lb6 = Label(root, text="Task 5", fg='white', bg='black', height=1, width=15, justify="left")

e = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)
e6 = Entry(root)
e7 = Entry(root)
e8 = Entry(root)
e9 = Entry(root)
e10 = Entry(root)


def AddTasks():
    file = open("todolist.txt", "a+")

    file.write("\n1: %s" % (e.get()))
    file.write(" Task 1: %s" % (e6.get()))
    file.write("\n2: %s" % (e2.get()))
    file.write(" Task 2: %s" % (e7.get()))
    file.write("\n3: %s" % (e3.get()))
    file.write(" Task 3: %s" % (e8.get()))
    file.write("\n4: %s" % (e4.get()))
    file.write(" Task 4: %s" % (e9.get()))
    file.write("\n5: %s" % (e5.get()))
    file.write(" Task 5: %s" % (e10.get()))

    file.close()

    msg = messagebox.showinfo("Done", "Successfully Added your tasks")


def Remaindme():
    file = open("todolist.txt", "r")
    now = datetime.today()
    d1 = now.strftime("%d/%m")
    flag = 0
    for line in file:
        if d1 in line:
            msg = messagebox.showinfo("Remainder", line)
            flag = flag + 1

    if flag==0:
        msg = messagebox.showinfo("Remainder", "You Have Nothing To Do Today")

txt = Text(root, fg='white', bg='black', height=7, width=55)
txt.insert(INSERT, "NOTE:\nAdd the date in format '%d/%m'\nAnd then the tasks in the next column.\nThis will help you to remaind your tasks as you added\nOn the specific date.")
Bu1 = Button(root, text="Add Tasks", command=AddTasks, fg='white', bg='green', height=1, width=15)
Bu2 = Button(root, text="Remaind Me", command=Remaindme, fg='white', bg='green', height=1, width=15)
Bu3 = Button(root, text="Exit", command=exit, fg='white', bg='green', height=1, width=15)

Lb.grid(row=0, padx=4, pady=5)
Lb7.grid(row=0, column=1, padx=4, pady=5)
Lb8.grid(row=0, column=2, padx=4, pady=5)
Lb2.grid(row=2, padx=4, pady=5)
Lb3.grid(row=3, padx=4, pady=5)
Lb4.grid(row=4, padx=4, pady=5)
Lb5.grid(row=5, padx=4, pady=5)
Lb6.grid(row=6, padx=4, pady=5)

e.grid(row=2, column=1, padx=4, pady=5)
e2.grid(row=3, column=1, padx=4, pady=5)
e3.grid(row=4, column=1, padx=4, pady=5)
e4.grid(row=5, column=1, padx=4, pady=5)
e5.grid(row=6, column=1, padx=4, pady=5)
e6.grid(row=2, column=2, padx=4, pady=5, columnspan=2)
e7.grid(row=3, column=2, padx=4, pady=5, columnspan=2)
e8.grid(row=4, column=2, padx=4, pady=5, columnspan=2)
e9.grid(row=5, column=2, padx=4, pady=5, columnspan=2)
e10.grid(row=6, column=2, padx=4, pady=5, columnspan=2)

Bu1.grid(row=9, column=1)
Bu2.grid(row=9, column=2)
Bu3.grid(row=9, column=4)

txt.grid(row=10, padx=2, pady=5)

root.mainloop()

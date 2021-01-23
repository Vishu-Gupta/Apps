"""
A program that stores the following book info:
Title, author
Year, ISBN

User Can:
View All entries
Search
Add Entry
Update selected
Delete
Close
"""
from tkinter import *

window = Tk()

l1= Label(window, text="Title")
l1.grid(row=0, column=0)

l2= Label(window, text="Author")
l2.grid(row=0, column=2)

l3= Label(window, text="Year")
l3.grid(row=1, column=0)

l4= Label(window, text="ISBN")
l4.grid(row=1, column=2)

title= StringVar()
e1= Entry(window, textvariable=title)
e1.grid(row=0, column=1)

author= StringVar()
e2= Entry(window,textvariable=author)
e2.grid(row=0, column=3)

year= StringVar()
e3= Entry(window, textvariable=year)
e3.grid(row=1, column=1)

isbn= StringVar()
e4= Entry(window, textvariable=isbn)
e4.grid(row=1, column=3)

b1=Button(window, text="View All", width=20)
b1.grid(row=2, column=3)
b2=Button(window, text="Search Entry", width=20)
b2.grid(row=3, column=3)
b3=Button(window, text="Add Entry", width=20)
b3.grid(row=4, column=3)
b4=Button(window, text="Update", width=20)
b4.grid(row=5, column=3)
b5=Button(window, text="Delete", width=20)
b5.grid(row=6, column=3)
b6=Button(window, text="Close", width=20)
b6.grid(row=7, column=3)

lb= Listbox(window, width=35)
lb.grid(row=2, column=0, rowspan=6, columnspan=2)

sb= Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

lb.configure(yscrollcommand=sb.set)
sb.configure(command=lb.yview)

window.mainloop()

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
import backend
window = Tk()
window.wm_title("BookStore")

def view_command():
    lb.delete(0,END)
    for row in backend.view_all():
        lb.insert(END, row) 

def search_command():
    lb.delete(0, END)
    for row in backend.search_book(title.get(), author.get(), year.get(), isbn.get()):
        lb.insert(END, row)

def add_command():
    backend.add_book(title.get(), author.get(), year.get(), isbn.get())
    lb.delete(0, END)
    lb.insert(END, (title.get(), author.get(), year.get(), isbn.get()))

def get_selected_row(event):
    try:
        global selected_tuple
        index= lb.curselection()[0]
        selected_tuple = lb.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass

def delete_command():
    backend.delete_entry(selected_tuple[0])

def update_command():
    backend.update_book(selected_tuple[0], title.get(), author.get(), year.get(), isbn.get())

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

b1=Button(window, text="View All", width=20, command=view_command)
b1.grid(row=2, column=3)

b2=Button(window, text="Search Entry", width=20, command=search_command)
b2.grid(row=3, column=3)

b3=Button(window, text="Add Entry", width=20, command=add_command)
b3.grid(row=4, column=3)

b4=Button(window, text="Update", width=20, command=update_command)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete", width=20, command=delete_command)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", width=20, command=window.destroy)
b6.grid(row=7, column=3)

lb= Listbox(window, width=35)
lb.grid(row=2, column=0, rowspan=6, columnspan=2)

sb= Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

lb.configure(yscrollcommand=sb.set)
sb.configure(command=lb.yview)

lb.bind('<<ListboxSelect>>',get_selected_row)

window.mainloop()

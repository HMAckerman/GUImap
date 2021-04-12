import mysqlPythonTesting as sqlPy
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askquestion

root = tk.Tk()
root.title("Nmap Database Program")
root.geometry("600x400")
frame = Frame(root)
frame.pack()

dbUser = StringVar()
dbPassword = StringVar()
target = StringVar()
flags = StringVar()
database = StringVar()

def myClick():
	dbUser = myUser.get()
	dpPassword = myPass.get()
	target = myTarget.get()
	flags = myFlags.get()
	database = myDatabase.get()

def exitApp():
	res = messagebox.askquestion('Exit Application',
								 'Do you really want to exit?')
	if res == 'yes':
		root.destroy()
	else:
		messagebox.showinfo('Return', 'Returning to main application.')

photo = PhotoImage(file = "media\nmaplogo.gif")
root.iconphoto(False, photo)

messagebox.showinfo("Database Created", sqlPy.create_database)

#This creates entry forms
tk.Label(frame, text = "Enter the User: ", font = 40).grid(row = 0)
myUser = tk.Entry(frame)
myUser.focus()
myUser.grid(row = 0, column = 1)

tk.Label(frame, text = "Enter Password: ", font = 40).grid(row = 1)
myPass = tk.Entry(frame, show = '*')
myPass.grid(row = 1, column = 1)

tk.Label(frame, text = "Enter the target(s) IP/URL: ", font = 40).grid(row = 2)
myTarget = tk.Entry(frame)
myTarget.grid(row = 2, column = 1)

tk.Label(frame, text = "Enter the nmap flags: ", font = 40).grid(row = 3)
myFlags = tk.Entry(frame)
myFlags.grid(row = 3, column = 1)

tk.Label(frame, text = "Enter the database to save to: ",
		font = 40).grid(row = 4)
myDatabase = tk.Entry(frame)
myDatabase.grid(row = 4, column = 1)

submitButton = ttk.Button(root, text = "Submit Data", command = lambda:[myClick,
						  askquestion('Confirm', 'Do you want to upload' +
						           ' results to the database?')])
submitButton.pack(pady = 10, padx = 10)

quit = Button(root, text = "Quit!", command = exitApp)
quit.pack(pady = 10, padx = 10)

root.mainloop()

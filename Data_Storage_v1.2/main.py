import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox

window = Tk()
window.withdraw()
window.title("Data Storage v1.2")
img = PhotoImage(file='logo.xbm')
window.tk.call('wm', 'iconphoto', window._w, img)

class loginPopup:

    key = False
    attemptChange = 5

    def __init__(self, master):
        top = self.top = Toplevel(master)
        top.title("Data Storage v1.2")
        img = PhotoImage(file='logo.xbm')
        top.tk.call('wm', 'iconphoto', top._w, img)
        top.geometry('{}x{}'.format(250, 200))
        top.resizable(width=False, height=False)

        self.label_user = Label(top, text='Enter Your Username', font = ('Roboto', 12), justify=CENTER, fg="cadetblue4")
        self.label_user.pack(pady=(15, 0))
        self.entry_user = Entry(top, width=30, fg="cadetblue4")
        self.entry_user.pack(pady=(10, 0))

        self.label_passw = Label(top, text='Enter Your Password', font = ('Roboto', 12), justify=CENTER, fg="cadetblue4")
        self.label_passw.pack(pady=(15, 0))
        self.entry_passw = Entry(top, show='*', width=30, fg="cadetblue4")
        self.entry_passw.pack(pady=(10, 0))

        self.btn = Button(top, text='Submit', font = ('Roboto', 14), command=self.login, fg="cadetblue4")
        self.btn.pack(pady=(15, 0))

    def login(self):
        self.user_value = self.entry_user.get()
        self.passw_value = self.entry_passw.get()

        user_access = 'nedim'
        passw_access = 'admin'

        if self.user_value == user_access and self.passw_value == passw_access:
            self.key = True
            self.top.destroy()
            window.deiconify()

        else:
            self.attemptChange -= 1

            if self.attemptChange == 0:
                window.quit()

            self.entry_passw.delete(0, 'end')

            messagebox.showerror("WRONG ATTEMPT!", "YOU HAVE {} ATTEMPTS REMAINING LEFT!".format(self.attemptChange))

class Data:

    def __init__(self,website,username,password,master):
        self.window = master
        self.website = website
        self.username = username
        self.password = password

        self.connection = sqlite3.connect("data_storage.db")

        self.cursor = self.connection.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS data_information (
                        website TEXT,
                        username TEXT,
                        password TEXT
                        ) """)

        self.connection.commit()

    def submit(self):
        self.connection = sqlite3.connect("data_storage.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute("INSERT INTO data_information VALUES (?,?,?)",(self.website, self.username, self.password))

        self.connection.commit()


class DataDisplay:

    def __init__(self, webDisplay, usernameDisplay, passwordDisplay, idDisplay, master):
        self.window = master
        self.website = webDisplay
        self.username = usernameDisplay
        self.password = passwordDisplay

        self.webDisplayLabel = Label(window, text=webDisplay, font=('Roboto', 10), fg="cadetblue4")
        self.userDisplayLabel = Label(window, text=usernameDisplay, font=('Roboto', 10), fg="cadetblue4")
        self.passwDisplayLabel = Label(window, text=passwordDisplay, font=('Roboto', 10), fg="cadetblue4")


    def display(self):
        self.webDisplayLabel.grid(row=8, sticky=W)
        self.userDisplayLabel.grid(row=8, column=1)
        self.passwDisplayLabel.grid(row=8, column=2)


def save():
    data = Data(webEntry.get(),usernameEntry.get(),passwordEntry.get(), window)
    data.submit()

    webEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)

    messagebox.showinfo("Process was succesfull!".upper(), "Data has added successfully!".upper())

def query():
    connection = sqlite3.connect("data_storage.db")
    cursor = connection.cursor()

    cursor.execute("SELECT *, rowid FROM data_information")
    records = cursor.fetchall()

    print_records = ''

    for record in records:
        print_records += str(f'ID: {record[3]}') + ' ' + str(record[0] + '\t' + record[1] + '\t' + record[2] + "\n\n")
        #print_records += str(record[0] + '\t' + record[1] + '\t' + record[2] + '\t' + str(record[3]) + "\n")

    connection.commit()
    connection.close()

    query_label = Label(window, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)


def delete():
    connection = sqlite3.connect("data_storage.db")
    cursor = connection.cursor()

    userChoice = tkinter.messagebox.askquestion("DELETE DATA", "DO YOU WANT TO DELETE THIS DATA?")

    if userChoice == 'yes':
        cursor.execute("DELETE FROM data_information WHERE oid = " + deleteBoxEntry.get())

        messagebox.showinfo("Process was succesfull!".upper(), "Data has deleted successfully! Please refresh your datas!".upper())

        connection.commit()
        connection.close()


loginScreen = loginPopup(window)

webEntry = Entry(window, width=35)
webEntry.grid(row=1, column=1)
usernameEntry = Entry(window, width=35)
usernameEntry.grid(row=2, column=1)
passwordEntry = Entry(window, width=35)
passwordEntry.grid(row=3, column=1)
deleteBoxEntry = Entry(window, width=10)
deleteBoxEntry.grid(row=6, column=1)

websiteLabel = Label(window, text='WEBSITE', font=('Roboto', 10), fg="cadetblue4")
websiteLabel.grid(row=1, column=0, padx=25, pady=5)
usernameLabel = Label(window, text='USERNAME', font=('Roboto', 10), fg="cadetblue4")
usernameLabel.grid(row=2, column=0, pady=5)
passwordLabel = Label(window, text='PASSWORD', font=('Roboto', 10), fg="cadetblue4")
passwordLabel.grid(row=3, column=0, pady=5)
deleteBoxLabel = Label(window, text='DELETE ID', font=('Roboto', 10), fg="cadetblue4")
deleteBoxLabel.grid(row=6, column=0)

submit_btn = Button(window, text="Add Record to Database", font = ('Roboto', 10), fg="cadetblue4", command=save)
submit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(window, text="Show Records", font = ('Roboto', 10), fg="cadetblue4", command=query)
query_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=130)

delete_btn = Button(window, text="Delete Record", font = ('Roboto', 10), fg="cadetblue4", command=delete)
delete_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=130)

#STORED DATA TEXT LABELS
# webDisplayLabel = Label(window, text='WEBSITE', font=('Roboto', 10), fg="cadetblue4")
# userDisplayLabel = Label(window, text='USERNAME', font=('Roboto', 10), fg="cadetblue4")
# passwDisplayLabel = Label(window, text='PASSWORD', font=('Roboto', 10), fg="cadetblue4")
# idDisplayLabel = Label(window, text='ID', font=('Roboto', 10), fg="cadetblue4")
#
# webDisplayLabel.grid(row=10, column=0)
# userDisplayLabel.grid(row=10, column=1)
# passwDisplayLabel.grid(row=10, column=2)
# idDisplayLabel.grid(row=10, column=3, padx=20, sticky=E)

window.mainloop()
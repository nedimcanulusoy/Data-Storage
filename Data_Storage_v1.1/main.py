from tkinter import *
from tkinter import messagebox
import tkinter.messagebox

window = Tk()
window.withdraw()
window.title("Data Storage v1.1")
storage = []

class loginPopup:

    key = False
    attemptChange = 5

    def __init__(self, master):
        top = self.top = Toplevel(master)
        top.title('LOGIN')
        top.geometry('{}x{}'.format(250, 100))
        top.resizable(width=False, height=False)

        self.label_passw = Label(top, text='Enter Your Password', font = ('Roboto', 12), justify=CENTER, fg="cadetblue4")
        self.label_passw.pack()
        self.entry_passw = Entry(top, show='*', width=30, fg="cadetblue4")
        self.entry_passw.pack(pady=7)

        self.btn = Button(top, text='Submit', font = ('Roboto', 14), command=self.login, fg="cadetblue4")
        self.btn.pack()

    def login(self):
        self.passw_value = self.entry_passw.get()

        passw_access = 'admin'

        if self.passw_value == passw_access:
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

    def __init__(self, website, username, password, master):
        self.window = master
        self.website = website
        self.username = username
        self.password = password

    def writeData(self):
        file = open('data.txt', 'a')
        file.write(self.website + ',' + self.username + ',' + self.password + ', \n')
        file.close()

class DataDisplay:

    def __init__(self, websiteDisplay, usernameDisplay, passwordDisplay, master, i):
        self.window = master
        self.i = i
        self.website = websiteDisplay
        self.username = usernameDisplay
        self.password = passwordDisplay

        self.label_websiteDisplay = Label(self.window, text=websiteDisplay, font = ('Roboto', 12), fg="cadetblue4")
        self.label_usernameDisplay = Label(self.window, text=usernameDisplay, font = ('Roboto', 12), fg="cadetblue4")
        self.label_passwordDisplay = Label(self.window, text=passwordDisplay, font = ('Roboto', 12), fg="cadetblue4")

        self.btn_delete = Button(self.window, text="X", fg="red", font = ('Roboto', 12), command=self.delete)

    def display(self):
        self.label_websiteDisplay.grid(row=6 + self.i, sticky=W)
        self.label_usernameDisplay.grid(row=6 + self.i, column=1)
        self.label_passwordDisplay.grid(row=6 + self.i, column=2, sticky=E)

        self.btn_delete.grid(row=6 + self.i, column=3, sticky=E)

    def delete(self):
        userChoice = tkinter.messagebox.askquestion("DELETE DATA", "DO YOU WANT TO DELETE THIS DATA?")

        if userChoice == 'yes':
            for i in storage:
                i.destroy()

            file = open('data.txt', "r")
            lines = file.readlines()
            file.close()

            file = open('data.txt', "r")
            count = 0

            for line in lines:
                if count != self.i:
                    file.write(line)
                    count += 1

            file.close()
            getData()

    def destroy(self):
        self.label_websiteDisplay.destroy()
        self.label_usernameDisplay.destroy()
        self.label_passwordDisplay.destroy()
        self.btn_delete.destroy()

def save():
    data = Data(entry_Website.get(), entry_Username.get(), entry_Password.get(), window)
    data.writeData()

    entry_Website.delete(0, "end")
    entry_Username.delete(0, "end")
    entry_Password.delete(0, "end")

    messagebox.showinfo("Process was succesfull!".upper(), "Data has added successfully!".upper())

def clearData():
    file = open('data.txt', 'w')
    file.close()

def getData():
    file = open('data.txt', 'r')
    count = 0

    for line in file:
        dataList = line.split(',')
        dataDisp = DataDisplay(dataList[0], dataList[1], dataList[2], window, count)
        storage.append(dataDisp)
        dataDisp.display()
        count += 1
    file.close()

loginScreen = loginPopup(window)

label_Data = Label(window, text="ADD DATA", font = ('Roboto', 12), fg="cadetblue4")
label_Website = Label(window, text="WEBSITE", font = ('Roboto', 12), fg="cadetblue4")
entry_Website = Entry(window, font = ('Roboto', 12), fg="cadetblue4")

label_Username = Label(window, text="USERNAME", font = ('Roboto', 12), fg="cadetblue4")
entry_Username = Entry(window, font = ('Roboto', 12), fg="cadetblue4")

label_Password = Label(window, text="PASSWORD", font = ('Roboto', 12), fg="cadetblue4")
entry_Password = Entry(window, font = ('Roboto', 12), fg="cadetblue4")

saveBtn = Button(window, text='SAVE THIS DATA', font = ('Roboto', 12), command=save, fg="cadetblue4")

label_Data.grid(columnspan=3, row=0)
label_Website.grid(row=1, sticky=E, padx=3)
label_Username.grid(row=2, sticky=E, padx=3)
label_Password.grid(row=3, sticky=E, padx=3)

entry_Website.grid(columnspan=3, row=1, column=1, padx=2, pady=2, sticky=W)
entry_Username.grid(columnspan=3, row=2, column=1, padx=2, pady=2, sticky=W)
entry_Password.grid(columnspan=3, row=3, column=1, padx=2, pady=2, sticky=W)

saveBtn.grid(columnspan=3, pady=4)

label_website2 = Label(window, text='Name: ', font = ('Roboto', 12), fg="cadetblue4")
label_username2 = Label(window, text='Email: ', font = ('Roboto', 12), fg="cadetblue4")
label_password2 = Label(window, text='Password: ', font = ('Roboto', 12), fg="cadetblue4")

label_website2 .grid(row=5, column=0)
label_username2.grid(row=5, column=1)
label_password2.grid(row=5, column=2)

getData()
window.mainloop()
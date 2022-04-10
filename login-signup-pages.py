import tkinter as tk
from tkinter import *
from tkinter import messagebox
from functools import partial
import hashlib
from typing import Type
import csv
from itertools import islice
from csv import reader
from click import password_option
import numpy as np
import pandas as pd
from operator import itemgetter
from pkg_resources import PEP440Warning
from Members import Members
from Coach import Coach

df = pd.read_csv('main-club-sheet.csv')
df.head()
name = df.name
timesAttended = df.timesAttended
phoneNumber = df.phoneNumber
address = df.address
paymentStatus = df.paymentStatus
timesUnpaid = df.timesUnpaid
getLoyaltyDisc = df.getLoyaltyDisc
noSkip = df.noSkip
multNoPay = df.multNoPay
amountPaid = df.amountPaid
amountDue = df.amountDue
advancedPayment = df.advancedPayment
latePayment = df.latePayment




def submit_btn():

    if password.get() == conf_pass.get():
        Label(signupScreen, text=" ").pack()
        Label(signupScreen, text="Succsefuly Registered ", fg = "green", font = ("Airel", 12)).pack()
        Button(signupScreen, text = "Login", width=15 , height=1, command = login).pack()
    else:
        Label(signupScreen, text="Passwords don't match ", fg = "red", font = ("Airel", 12)).pack()



def signup(): 
    global signupScreen
    signupScreen = Toplevel(tkWindow)
    signupScreen.title('Sign Up!')
    signupScreen.geometry("700x700+600+300")

    global user_entry
    global pass_entry
    global conf_passEntry
    global password
    global username
    global conf_pass

    username = StringVar()
    password = StringVar()
    conf_pass = StringVar()

    Label(signupScreen, text="Please enter the required fields: ").pack()
    Label(signupScreen, text=" ").pack()

    Label(signupScreen, text="Username:").pack()
    user_entry = Entry(signupScreen, textvariable = username)
    user_entry.pack()

    Label(signupScreen, text="Password").pack()
    pass_entry = Entry(signupScreen, textvariable = password)
    pass_entry.pack()

    Label(signupScreen, text="Confirm Password").pack()
    conf_passEntry = Entry(signupScreen, textvariable = conf_pass)
    conf_passEntry.pack()

    Label(signupScreen, text=" ").pack()
    Button(signupScreen, text = "Submit", width=15 , height=1, command = submit_btn).pack()


    if conf_pass.get() == password.get():
        print("Successful login!")
    # elif not conf_pass.get():
    #     print("You must fill in all fields")
    # elif not password.get():
    #     print("You must fill in all fields")
    # elif not username.get():
    #     print("You must fill in all fields")
    else:
        print('Passwords must match \n')
        signup()
    print('You have registered successfully!')




def signupWindow():
        tkWindow.destroy()
        signupWindow_main = Tk()

        Label(signupWindow_main, text = "Sign up").pack()

        #spacer label
        Label(signupWindow_main, text = " ").pack()

        #username label and text entry box
        usernameLabel = Label(signupWindow_main, text="User Name").pack()
        username = StringVar()
        usernameEntry = Entry(signupWindow_main, textvariable=username).pack()

        #password label and text entry box
        passwordLabel = Label(signupWindow_main, text="Password").pack()
        password = StringVar()
        passwordEntry = Entry(signupWindow_main, textvariable=password).pack()


        #password confirmation label and text entry box
        conf_passLabel = Label(signupWindow_main, text="Confirm Password").pack()
        conf_pass = StringVar()
        conf_passEntry = Entry(signupWindow_main, textvariable=conf_pass).pack()


        #dumy boxes for address and phone number
        Label(signupWindow_main, text="Address").pack()
        Entry(signupWindow_main).pack()
        Label(signupWindow_main, text="Phone Number").pack()
        Entry(signupWindow_main).pack()


        Button(signupWindow_main, text = "Sign up", command=signup).pack() 

        
        signupWindow_main.geometry("700x700+600+300")
        signupWindow_main.mainloop()


SortedPaidMember = [] #a list that will be sorted depending on how many times a member has paid/unpaid
member1=0

# def createMember(username): #this function reads the csv file and if their accountType is member and username is equal to the currently logged in user, 
#     #it makes them a member of the Members class (this is basically what Ollie and I discussed on discord)
#     with open('main-club-sheet.csv', 'r') as read_obj:
#         csv_reader = reader(read_obj)
#         for row in csv_reader:
#             #print(row)
#             if(row[12] == "member"):
#                 SortedPaidMember.append([row[0], row[1], row[3], row[4],row[5], row[6], row[8], row[10], row[13], row[14]])
#             if(row[12] == "member" and row[1] == username):
#                 global member1
#                 member1 = Members(row[0], row[3], row[4], row[6], row[8], row[10], row[13], row[14], row[1], row[2], row[20])
#                 member1.notification()
#             elif(row[12] == "coach" and row[1] == username):
#                 member1 = Coach(row[0], row[3], row[4], row[6], row[8], row[10], row[13], row[14], row[1], row[2], row[20])
#         if type(member1) == Coach:
#             member1.logMembers(SortedPaidMember)
#             member1.sortUnpaidStatus(SortedPaidMember)







def login():
    global screen2
    screen2 = Toplevel(tkWindow)
    screen2.title('Login')
    screen2.geometry("700x700+600+300")
    Label(screen2, text = "Enter your username and password below to sign in").pack()
    Label(screen2, text = " ").pack()

    global verify_user
    global verify_pass
    global user_entry2
    global pass_entry2

    verify_user = StringVar()
    verify_pass = StringVar()

    Label(screen2, text="Username:").pack()
    user_entery2 = Entry(screen2, textvariable = verify_user)
    user_entery2.pack()
    Label(screen2, text=" ").pack()
    Label(screen2, text="Password:").pack()
    pass_entery2 = Entry(screen2,  show='*', textvariable = verify_pass)
    Label(screen2, text=" ").pack()
    pass_entery2.pack()
    Label(screen2, text=" ").pack()
    Button(screen2, text = "Login", width = 15, height=1, command = verifyLogin).pack()


def verifyLogin():

    global user_entry2
    global pass_entry2
    global signupScreen

    username2 = verify_user.get()
    password2 = verify_pass.get()

    with open('main-club-sheet.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            if username2 == row[1]:
                foundUser = True
                if password2 == row[2]:
                    print('Successful login!')
                    # createMember(username2) #now as we create an instance of the member class
                else:
                    Label(screen2, text="Passwords is incorrect ", fg = "red", font = ("Airel", 12)).pack()
                    # login()
        if not foundUser:
            Label(screen2, text="Please enter a valid username ", fg = "red", font = ("Airel", 12)).pack()
            # login()


def mainScreen():
    global tkWindow
    tkWindow = Tk()
    tkWindow.geometry("700x700+600+300")

    Label(text = 'Welcome to the Salsa Dancing Club Online Portal!', bg='pink', width = "300", height= "2", font = ("Airel", 13)).pack()
    Label(text = "").pack()
    loginButton = Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    signupButton = Button(text="Sign up", height="2", width="30", command = signup).pack()

    tkWindow.mainloop()


def memberScreen():
    global tkWindow
    tkWindow = Tk()
    tkWindow.geometry("700x700+600+300")

    Label(text = 'Welcome to your account!', bg='pink', width = "300", height= "2", font = ("Airel", 13)).pack()
    Label(text = "").pack()
    Label(text = 'Amount Owing: ')
    loginButton = Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    signupButton = Button(text="Sign up", height="2", width="30", command = signup).pack()




def run_function():
    mainScreen()
run_function()

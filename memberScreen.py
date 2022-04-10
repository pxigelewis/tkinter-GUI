import tkinter as tk
from tkinter import *
from tkinter import messagebox
from functools import partial
import hashlib
from turtle import clear
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

# global screen3
# screen3 = Tk()
# screen3.geometry("700x700+600+300")



def membersAttended():
    
    maxAttended = (timesAttended >= 35.0)
    with open ('main-club-sheet.csv', 'rt', encoding='utf8') as f:
        reader = csv.DictReader(f)
        for row in islice(reader, 10):
            print(row['name'])   
    membersAttended()
            


def mostAttended():
    df[['name', 'timesAttended']]


def accountOverviewScreen():
    global actOverview
    actOverview = Toplevel(mainMemberScreen)
    actOverview.title('Account Overview')
    actOverview.geometry("700x700+600+300")

    Label(actOverview, text = ' ').pack()
    Label(actOverview, text = ' ').pack()
    Label(actOverview, text = ' ').pack()
    Label(actOverview, text = ' ').pack()
    Label(actOverview, text = 'Name: ').pack()   #i think we can pull username from login
    Label(actOverview, text = ' ').pack()
    Label(actOverview, text = 'Payment status: ').pack()
    Label(actOverview, text = ' ').pack()
    Label(actOverview, text = 'Amount due (if applicable): ').pack()

    with open ('main-club-sheet.csv', 'rt', encoding='utf8') as f:
        for i in name:
            print(name[i])


    mainMemberScreen.mainloop()


def balaceDue():
    for i in paymentStatus:
        if paymentStatus == 0:
            print(name[i])
        else:
            print('error')


def submit_btn2():
    ccnLength = len(ccnEntry.get())
    expLength = len(expiryEntry.get())
    cvvLength = len(ccvEntry.get())

    if (ccnLength != 16):
        Label(paymentScreen, text="Please enter a valid credit card number ", fg = "red", font = ("Airel", 12)).pack()
    elif (expLength != 4):
        Label(paymentScreen, text=" ").pack()
        Label(paymentScreen, text="Please enter a valid expiry date ", fg = "red", font = ("Airel", 12)).pack()
    elif (cvvLength != 3):
        Label(paymentScreen, text=" ").pack()
        Label(paymentScreen, text="Please enter a valid ccv ", fg = "red", font = ("Airel", 12)).pack()
    else:
        Label(paymentScreen, text=" ").pack()
        Label(paymentScreen, text="Payment Successful ", fg = "green", font = ("Airel", 12)).pack()
   



def makeAPayment():
    global paymentScreen
    paymentScreen = Toplevel(mainMemberScreen)
    paymentScreen.title('Make a Payment')
    paymentScreen.geometry("700x700+600+300")

    global nameEntry
    global addressEntry
    global ccnEntry
    global expiryEntry
    global ccvEntry

    name = StringVar()
    address = StringVar()
    ccn = StringVar()
    expiry = StringVar()
    ccv = StringVar()

    Label(paymentScreen, text = 'Make a Payment', bg='pink', width = "300", height= "2", font = ("Airel", 13)).pack()

    Label(paymentScreen, text = ' ').pack()

    Label(paymentScreen, text = 'Name: ').pack()
    nameEntry = Entry(paymentScreen, textvariable = name)
    nameEntry.pack()

    Label(paymentScreen, text = 'Address: ').pack()
    addressEntry = Entry(paymentScreen, textvariable = address)
    addressEntry.pack()

    Label(paymentScreen, text = 'Credit Card Number: ').pack()
    ccnEntry = Entry(paymentScreen, textvariable = ccn)
    ccnEntry.pack()

    Label(paymentScreen, text = 'Expiry: ').pack()
    expiryEntry = Entry(paymentScreen, textvariable = expiry)
    expiryEntry.pack()

    Label(paymentScreen, text = 'CVV: ').pack()
    ccvEntry = Entry(paymentScreen, textvariable = ccv)
    ccvEntry.pack()

    Label(paymentScreen, text=" ").pack()
    Button(paymentScreen, text = "Submit", width=15 , height=1, command = submit_btn2).pack()
    


# def coachScreen():

global mainMemberScreen
mainMemberScreen = Tk()
mainMemberScreen.title("Welcome to your member account")
mainMemberScreen.geometry("700x700+600+300")


Label(text = 'Welcome to your account!', bg='pink', width = "300", height= "2", font = ("Airel", 13)).pack()
Label(text = "").pack()
Label(text = 'Please pick from the list of options below: ').pack()
#function here to display amount owing
top10Members = Button(text="Account overview", height="2", width="30", command = accountOverviewScreen).pack()   #amount owing, amount paid, number of classes attended, etc
Label(text="").pack()
numTimesAttended = Button(text="Balace due", height="2", width="30", command = balaceDue).pack()
Label(text="").pack()
loginButton = Button(text="Make a Payment", height="2", width="30", command = makeAPayment).pack()
Label(text="").pack()

mainMemberScreen.mainloop()

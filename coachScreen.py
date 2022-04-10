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


def attendingNextClass():
    with open ('main-club-sheet.csv', 'rt', encoding='utf8') as f:
        if noSkip == 1.0:
            print(name)
        else:
            print('error')


def allMembersScreen():
    global allMemScreen
    allMemScreen = Toplevel(mainCoachScreen)
    allMemScreen.title('All Members')
    allMemScreen.geometry("700x700+600+300")

    Button(allMemScreen, text = "Click to see a list of all members", width = 25, height=3, command = mostAttended).pack()
    mostAttended()
    # mainCoachScreen.mainloop()


# def coachScreen():

global mainCoachScreen
mainCoachScreen = Tk()
mainCoachScreen.geometry("700x700+600+300")


Label(text = 'Welcome to your account!', bg='pink', width = "300", height= "2", font = ("Airel", 13)).pack()
Label(text = "").pack()
Label(text = 'What would you like to check? ').pack()
#function here to display amount owing
top10Members = Button(text="Top 10 Attending Members", height="2", width="30", command = allMembersScreen).pack()
Label(text="").pack()
numTimesAttended = Button(text="Number of Times Each Member Has Attended", height="2", width="30", command = mostAttended).pack()
Label(text="").pack()
loginButton = Button(text="Members Signed Up Your Next Class", height="2", width="30", command = attendingNextClass).pack()
Label(text="").pack()

mainCoachScreen.mainloop()

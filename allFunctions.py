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


def membersAttended():
    
    maxAttended = (timesAttended >= 35.0)
    with open ('main-club-sheet.csv', 'rt', encoding='utf8') as f:
        reader = csv.DictReader(f)
        for row in islice(reader, 10):
            print(row['name'])   
membersAttended()
            



def mostAttended():
    print(df[['name', 'timesAttended']])
mostAttended()


def latePayment():
    print(df.loc[df['latePayment'] == True]['username'])
latePayment()



def attendingNextClass():
    attendingNextClass = (timesAttended >= 20.0)
    with open ('main-club-sheet.csv', 'rt', encoding='utf8') as f:
        for i in timesAttended:
            if attendingNextClass:
                print(df[['name', 'phoneNumber', 'address', 'paymentStatus']])
        for i in noSkip:
          if attendingNextClass:
              print(df[['name', 'phoneNumber', 'address', 'paymentStatus']])
          else:
              print('error')

attendingNextClass()

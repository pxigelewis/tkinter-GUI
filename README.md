# tkinter-GUI

This is a collection of files for a GUI applications that allows members and coached of a 'Salsa Dancing Club' to check various information related to 
their account. 

This is my contribution to the CPS406: Introduction to Software Engineering final project.

Note: these are not completely finished files and will be updated on April 15th upon completion of this assigment.

## An overview of each file:

login-signup-pages.py: This page allows a user to login or sign up for an account. During sign up, there is a check to make sure both password submissions 
match, and during login, the users username and password are checked against a database of existing users.

memberScreen.py: This is the screen that a normal member of the club would see upon login. From here, they're able to see an account overview, check their 
balance, or make a payment if they have a balance owing.

coachScreen.py: This is the screen a coach would see upon logging into the system. They are able to look at the top attending members, how many classes 
each member has attended, and who is signed up for their next class.

allFunctions.py: A collection of functions that will be implemented in the coachScreen.py file

main-club-sheet.csv: A .csv sheet I created that contains account/member information for 50 club members. This is used for testing the code as well as in 
all of the created functions.

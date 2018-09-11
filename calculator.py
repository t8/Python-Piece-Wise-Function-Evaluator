## Piece Wise Function Evaluator
## Tate Berenbaum
## Sept 8 2018
## Evaluates a piece-wise function based on a user-inputted x-value

# To do the math:
import math

# To execute system commands
import os

# To test if your system has necessary packages
import pkgutil
# Testing if your system has necessary packages
if not pkgutil.find_loader("pyfiglet") and not pkgutil.find_loader("terminal_banner"):
    print("Installing dependencies!")
    # Cloning a python font repository for commandline usage
    os.system("pip install pyfiglet")
    # Cloning a python help menu repository for commandline usage
    os.system("pip install terminal-banner")

# Importing the new packages
from pyfiglet import Figlet
import terminal_banner


# This function does the calculations necessary to retrieve a correct y-value for the given x-value
def doDaMath(xVal):
    # Making this string into a valid float variable (float is a numeric variable)
    xFloat = float(xVal)
    y = 0

    # Now we need to determine what interval the x-value fits in
    if xFloat >= 4:
        # Calculating y-value for 3rd interval
        y = math.sqrt(xFloat - 3)
    elif 1 <= xFloat < 4:
        # Calculating y-value for 2nd interval
        y = (2 * xFloat) + 5
    elif xFloat < 1:
        # Calculating y-value for 1st interval
        y = math.pow(xFloat - 1, 2)

    return round(y, 3)


# Writing the title text
f = Figlet(font='speed')
print (f.renderText('Piece Wise Function Evaluator'))

# Showing menu after each run
wantToQuit = False
while not wantToQuit:
    # Showing description banner
    desc = "This script evaluates the following piece-wise function based on a user-inputted x-value! \n\n" \
           "       (x - 1)^2     if   x < 1\n" \
           "f(x) = 2x + 5        if   1 <= x < 4\n" \
           "       sqrt(x - 3)   if   4 <= x < 100\n\n" \
           "Please type 'r' to run or any other character to quit!"
    descBanner = terminal_banner.Banner(desc)
    print(descBanner)

    # Receiving user-confirmation that they actually want to run the program
    confirmation = input()
    # Analyzing inputted variable
    if confirmation != "r":
        wantToQuit = True
        break

    hasNotAnswered = True
    while hasNotAnswered:
        # Showing x-input description and getting user-input
        xVarDesc = "Please input your x-value for the function! \n\n" \
                   "Note: This value must be within the domain: {x | x < 100}"
        xVarDescBanner = terminal_banner.Banner(xVarDesc)
        print(xVarDescBanner)

        xInput = input()
        xInpNum = xInput.replace('.', '', 1)
        xInpNum = xInpNum.replace('-', '', 1)
        # Ensuring inputted variable is a number
        if xInpNum.isdigit() and float(xInput) < 100:
            hasNotAnswered = False
            continue
        else:
            print("\nYou did not answer with a valid number! Please try again!")
    # Calling function 'doDaMath' and passing in the inputted variable
    answer = doDaMath(xInput)
    answerDesc = "\n The value of the function at " + xInput + " is " + str(answer) + "\n\n" \
                 "If you would like to try another x-value, please click 'enter' on your keyboard \n" \
                 "Type any other character and the program will exit! \n"
    answerDescBanner = terminal_banner.Banner(answerDesc)
    print(answerDescBanner)
    # Finding if user wants to continue or quit
    exit = input()
    if exit != "":
        wantToQuit = True
        break

f2 = Figlet(font='big')
print (f2.renderText("Thanks!"))
print("Thank you for using my program broooo")

'''
Program:               ATM Script
Author:                
Class:                 IT-140-T5093 Introduction to scripting 18EW5
Instructor             
Date:                  10 Jun 2018
Description:        A program that by collecting customers data from the INPUT of currency. 
                    the program OUTPUTS the total of weather a Deposit has been made or withdrawn.
                    Finally, it can let the customer know how much currency they currently have in there account.
'''

import sys

account_balance=float(500.25)

print("")
def print_balance():
    print(account_balance)
def deposit(amount):
    global account_balance
    print("Begining Balance: "+str(round(account_balance,2)))
    account_balance+=amount
def withdrawal(amount):
    global account_balance
    if amount<=account_balance:
        account_balance-=amount
        print("Withdrawal amount was $"+str(amount)+", current balance is $"+str(round(account_balance,2)))
    else:
        print(str(amount)+"is greater than your account balance of $"+str(round(account_balance,2)))

def menu():
  
    print("What would you like to do?")
    print("B Account balance")
    print("W Withdraw amount")
    print("D Deposit amount")
    print("Q Quit")
while True:
    menu()
    userchoice=input()
    if userchoice == "B" or userchoice == "b":
        print("Your account balance:"+str(round(account_balance,2)))
    elif userchoice in ["d", "D"]:
        deposit_amount=float(input("How much would you like to deposit today?"))
        deposit(deposit_amount)
        print("Deposit was $"+str(deposit_amount)+", account balance is $"+str(round(account_balance,2)))
    elif userchoice in ["w", "W"]:
        withdrawal_amount=float(input("How much would you like to withdraw today?"))
        withdrawal(withdrawal_amount)
    elif userchoice in ['q', 'Q']:
        print("Thank you for banking with us")
        break

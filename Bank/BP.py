import os
import json
import random

clear = lambda: os.system("cls")  # on Windows System
# os.system('clear') #on Linux System

with open("data.json", "r") as file:
    dbCustomers = json.load(file)

Customers = list(dbCustomers)


def updateAccountData() -> None:
    if Customers != dbCustomers:
        with open("data.json", "w") as file:
            json.dump(Customers, file, indent=4)


def createAccount() -> None:
    if len(Customers) == 0:
        accountNumber = random.randint(1000000, 9999999)
        Name = input("Enter Name: ")
        credit = int(input("Enter opening amount: "))
        customer = [accountNumber, Name, credit]
        Customers.append(customer)
    else:
        numberPresent = True
        while numberPresent == True:
            accountNumber = random.randint(1000000, 9999999)
            print("account number selected:", accountNumber)
            for i in range(len(Customers)):
                if Customers[i][0] == accountNumber:
                    break
                else:
                    numberPresent = False
        Name = input("Enter Name: ")
        credit = int(input("Enter opening amount: "))
        customer = [accountNumber, Name, credit]
        Customers.append(customer)
    print("--:Account created:--")
    accountInformation(-1)
    updateAccountData()


def searchAccountByNumber(Number: int) -> int | None:
    for i in range(len(Customers)):
        if Customers[i][0] == Number:
            return i


def deposit(idx: int, amount: int) -> None:
    if amount > 0:
        Customers[idx][2] += amount
        print("₹" + str(amount) + " deposited to account")
        print("Current Balance: ₹" + str(Customers[idx][2]))
        input("Press Enter to continue")
        updateAccountData()

    else:
        print("Invalid amount entered")
        input("Press Enter to continue")


def withdraw(idx: int, amount: int) -> None:
    if amount > 0:
        if Customers[idx][2] > amount:
            Customers[idx][2] -= amount
            print("₹" + str(amount) + " withdrawn from account")
            print("Current Balance: ₹" + str(Customers[idx][2]))
            input("Press Enter to continue")
            updateAccountData()
        else:
            print("Insufficient account balance")
            print("Current Balance: ₹" + str(Customers[idx][2]))
            input("Press Enter to continue")
    else:
        print("Invalid amount entered")
        input("Press Enter to continue")


def accountInformation(Idx: int) -> None:
    print(
        "Customer Details:\nAccount Number:",
        Customers[Idx][0],
        "\nCustomer Name:",
        Customers[Idx][1],
        "\nAccount Balance: " + "₹" + str(Customers[Idx][2]),
    )


def accountOptions(index: int) -> None:
    print("\n**_Account Options_**")
    print("a. Deposit Money")
    print("b. Withdraw Money")
    print("c. Delete Account")
    print("q. quit")
    c2 = input("Chose Option: ")
    clear()
    if c2 == "a":
        Amount = int(input("Enter amount: "))
        deposit(index, Amount)
    elif c2 == "b":
        Amount = int(input("Enter amount: "))
        withdraw(index, Amount)
    elif c2 == "c":
        Customers.pop(index)
        print("Account Deleted !!")
        input("Press Enter to continue")
        updateAccountData()
    elif c2 == "q":
        print("Exiting Program")
    else:
        print("Invalid choice")


while True:
    clear()
    print("Bank Options:")
    print("a. Search existing customer")
    print("b. Add a customer")
    print("c. Check Database")
    print("q. quit")
    choice1 = input("Enter your choice: ")
    clear()
    if choice1 == "a":
        if len(Customers) == 0:
            print("No customers found\n--Options--\na: Add customer\nq: quit ")
            c = input()
            clear()
            if c == "q":
                print("Exiting program")
                break
            elif c == "a":
                createAccount()
                input("Press Enter to continue")
            else:
                print("Invalid choice")
                break
        else:
            accountNumber = int(input("Enter account Number: "))
            idx2 = searchAccountByNumber(accountNumber)
            if idx2 == None:
                print("Account not found !!")
                input("Press Enter to continue")
            else:
                accountInformation(idx2)
                accountOptions(idx2)
    elif choice1 == "b":
        createAccount()
        input("Press Enter to continue")
    elif choice1 == "c":
        print("Total number of accounts:", len(Customers))
        print("All Acounts: ")
        for i in range(len(Customers)):
            print(Customers[i])
        input("Press Enter to continue")
    elif choice1 == "q":
        print("Exiting programe")
        break
    else:
        print("invalid choice\nTry Again")
        input("Press Enter to continue")

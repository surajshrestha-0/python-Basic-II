"""
Imagine you are designing a banking application.
What would a customer look like?
What attributes would she have?
What methods would she have?
"""


class Customer:
    def __init__(self, name, gender, age, address, email_address, contact_number, account_number, account_type,
                 balance):
        self.name = name
        self.gender = gender
        self.age = age
        self.address = address
        self.email_address = email_address
        self.contact_number = contact_number
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    # Function to deposit amount
    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    # Function to withdraw the amount
    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance ")

    # Function to display the amount
    def display(self):
        print("\nAccount Holder : ", self.name, "\t\t Account Name : ", self.account_number)
        print("Account Holder : ", self.gender, "\t\t\t\t Age : ", self.age)
        print("Email Address : ", self.email_address, "\t Contact Number : ", self.contact_number)
        print("Account Number : ", self.account_number, "\t\t Account Type : ", self.account_type)
        print("Net Available Balance : ", self.balance)


# creating an object of class
c = Customer('Sita Thapa', 25, 'Female', 'Kathmandu', 'sita@gmail.com', '+977-9841111111', '009123124', 'saving', 2000)
print("Welcome To ABC Bank!")
print("Please select -\n 1. To Deposit\n 2. To Withdraw \n 3.View Account Details")
# Take input from the user
select = int(input("Select operations form 1, 2, 3:"))

if select == 1:
    c.deposit()
elif select == 2:
    c.withdraw()
elif select == 3:
    c.display()
else:
    print("Invalid input! Please select Vaild operation and try again!!")
